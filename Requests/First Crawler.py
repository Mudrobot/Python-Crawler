'''
from urllib.request import urlopen

url="http://www.baidu.com"
resp=urlopen(url)
#print(resp.read().decode("utf-8"))
f=open("Mybaidu.html",mode="w",encoding="utf-8")
f.write(resp.read().decode("utf-8"))
print("over")
resp.close()#关闭会话，防止后续使用爬虫出现无法访问的情况
'''
import requests
url="http://www.baidu.com"
s=requests.Session()
resp=s.get(url)
resp.encoding="utf-8"# windows系统必须加这个否则读取中文的时候可能会出现乱码的情况
print(resp.text)