import requests
url="https://jinshuju.net/f/NKh64k/s/3dFMki"
#反爬可以在这里加一个头
dic={# 这里dic代表的时请求头，是一个字典变量
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
}
#然后下面的请求改一下就可以了
for i in range(2):
    dat={
        "q[0][field_2]": "2020020908003",
        "q[0][field_3]" : "江昊林"
    }
    resp=requests.get(url,headers=dic,data=dat)
    #resp=requests.get(url)
    resp.encoding="utf-8"# windows系统必须加这个否则读取中文的时候可能会出现乱码的情况
    #print(resp.text)
    f=open("RAW.html","w",encoding="utf-8")#windows系统一定要写encoding="utf-8"
    f.write(resp.text)
    print("over")
    resp.close()