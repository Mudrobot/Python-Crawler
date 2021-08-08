#1.如何提取单个界面的数据
#2、用线程池提取多个页面的数据
import requests
from lxml import etree
url="http://www.xinfadi.com.cn/getPriceData.html"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
}
data={
    "limit": 20,
    "current": 1
}
for i in range(3):
    data["current"]=i+1
    resp=requests.post(url,headers=headers,data=data)
    resp.encoding="utf-8"
    for ingridient in resp.json()['list']:
        print(ingridient["prodName"])
    print("_______________________________________")