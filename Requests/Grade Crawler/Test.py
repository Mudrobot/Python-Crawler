import requests
import xlrd
from lxml import etree
import xlsxwriter as xw
import time
def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("工试")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['学号','姓名']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j]["q[0][field_2]"], data[j]["q[0][field_3]"]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表
dataa = xlrd.open_workbook('RawSource.xlsx')
table = dataa.sheets()[0]#读取当前xlsx中的第一个sheet内容 
url="https://jinshuju.net/f/NKh64k/s/3dFMki"
datt=[]
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
}
def judge(ddata):
    resp=requests.get(url,headers=headers,data=ddata)
    #resp=requests.get(url)
    resp.encoding="utf-8"# windows系统必须加这个否则读取中文的时候可能会出现乱码的情况
    #print(resp.text)
    f=open("RAW_judge.html","w",encoding="utf-8")#windows系统一定要写encoding="utf-8"
    f.write(resp.text)
    parser = etree.HTMLParser(encoding='utf-8')#需要解析一下
    tree = etree.parse('RAW_judge.html', parser=parser)
    datasource=tree.xpath("/html/body")
    dic={}
    for data in datasource:
        result=data.xpath(".//tr[@data-field='field_1']/@data-value")
        if result==[]:
            return 0
        else:
            return 1
cnt=0
for rown in range(table.nrows):#读取表的每一列
    if rown==0 or rown==1:
        continue
    for i in range(30):
        num=int(table.cell_value(rown,1))*1000+i+1
        num=str(num)
        name=table.cell_value(rown,2)
        dat={
            "q[0][field_2]": num,#班号
            "q[0][field_3]" :name #姓名
        }
        if judge(dat)==1:
            cnt+=1
            print("GOT one!",cnt)
            datt.append(dat)
            break
print(datt)
print("over")
xw_toExcel(datt,"花名册.xlsx")