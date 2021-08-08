import requests
import xlrd
from lxml import etree
import xlsxwriter as xw
import time
dataa = xlrd.open_workbook('花名册.xlsx')
table = dataa.sheets()[0]#读取当前xlsx中的第一个sheet内容 
url="https://jinshuju.net/f/NKh64k/s/3dFMki"
#反爬可以在这里加一个头
headers={# 这里dic代表的时请求头，是一个字典变量
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
}
datt=[]#最后总的成绩单
def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("工试")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['学号','姓名','平均绩点','大学物理Ⅰ','微积分Ⅱ','电路分析与电子线路','中国近代史纲要','英语','电路实验Ⅰ','电装实习','大学体育Ⅱ','加权平均分（公式）','加权平均分（数值）','专业排名','工试排名']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j]["学号"], data[j]["姓名"], data[j]["平均绩点"], data[j]["大学物理Ⅰ"], data[j]["微积分Ⅱ"], data[j]["电路分析与电子线路"], data[j]["中国近代史纲要"], data[j]["英语"], data[j]["电路实验Ⅰ"], data[j]["电装实习"], data[j]["大学体育Ⅱ"], data[j]["加权平均分（公式）"], data[j]["加权平均分（数值）"], data[j]["专业排名"], data[j]["工试排名"]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表
def GetData(ddata):
    #然后下面的请求改一下就可以了
    resp=requests.get(url,headers=headers,data=ddata)
    #resp=requests.get(url)
    resp.encoding="utf-8"# windows系统必须加这个否则读取中文的时候可能会出现乱码的情况
    #print(resp.text)
    f=open("RAW.html","w",encoding="utf-8")#windows系统一定要写encoding="utf-8"
    f.write(resp.text)
    print("Crawl over")
    #resp.close()
    ### 抓取结束
    ### 开始提取重要的信息
    parser = etree.HTMLParser(encoding='utf-8')#需要解析一下
    tree = etree.parse('RAW.html', parser=parser)
    datasource=tree.xpath("/html/body")
    dic={}
    
    for data in datasource:
        result=data.xpath(".//tr[@data-field='field_1']/@data-value")
        if result==[]:
            print("Empty")
            break
        dic.update({"序号":result[0]})
        result=data.xpath(".//tr[@data-field='field_2']/@data-value")
        dic.update({"学号":result[0]})
        result=data.xpath(".//tr[@data-field='field_3']/@data-value")
        dic.update({"姓名":result[0]})
        result=data.xpath(".//tr[@data-field='field_4']/@data-value")
        dic.update({"平均绩点":result[0]})
        result=data.xpath(".//tr[@data-field='field_5']/@data-value")
        dic.update({"大学物理Ⅰ":result[0]})
        result=data.xpath(".//tr[@data-field='field_6']/@data-value")
        dic.update({"微积分Ⅱ":result[0]})
        result=data.xpath(".//tr[@data-field='field_7']/@data-value")
        dic.update({"电路分析与电子线路":result[0]})
        result=data.xpath(".//tr[@data-field='field_8']/@data-value")
        dic.update({"中国近代史纲要":result[0]})
        result=data.xpath(".//tr[@data-field='field_9']/@data-value")
        dic.update({"英语":result[0]})
        result=data.xpath(".//tr[@data-field='field_10']/@data-value")
        dic.update({"电路实验Ⅰ":result[0]})
        result=data.xpath(".//tr[@data-field='field_11']/@data-value")
        dic.update({"电装实习":result[0]})
        result=data.xpath(".//tr[@data-field='field_12']/@data-value")
        dic.update({"大学体育Ⅱ":result[0]})
        result=data.xpath(".//tr[@data-field='field_13']/@data-value")
        dic.update({"加权平均分（公式）":result[0]})
        result=data.xpath(".//tr[@data-field='field_14']/@data-value")
        dic.update({"加权平均分（数值）":result[0]})
        result=data.xpath(".//tr[@data-field='field_15']/@data-value")
        dic.update({"专业排名":result[0]})
        result=data.xpath(".//tr[@data-field='field_16']/@data-value")
        dic.update({"工试排名":result[0]})
        return dic
for rown in range(table.nrows):#读取表的每一列
    #time.sleep(1)                                             # 设置等待时间为1s
    if rown==0:
        continue
    dat={
        "q[0][field_2]": table.cell_value(rown,0),
        "q[0][field_3]" :table.cell_value(rown,1)
    }
    dicc=GetData(dat)
    if dicc!={}:
        datt.append(dicc)
    print("over",rown+1)
if datt!=[]: 
    xw_toExcel(datt,"成绩表.xlsx")
print("All Over!")