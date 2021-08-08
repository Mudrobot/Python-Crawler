html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Title</title>
</head>
<body>
    <ul>
        <li><a href="http://www.baidu.com">百度</a></li>
        <li><a href="http://www.google.com">谷歌</a></li>
        <li><a href="http://www.sougou.com">搜狗</a></li>
    </ul>
    <ol>
        <li><a href="feiji">飞机</a></li>
        <li><a href="dapao">大炮</a></li>
        <li><a href="huoche">火车</a></li>
    </ol>
    <div class="job">李嘉诚</div>
    <div class="common">胡辣汤</div>
</body>
</html>
"""
from lxml import etree
tree=etree.XML(html)# 加载这个字符串作为XML
### Test1 拿到ul中三个超链接中的文字
result1=tree.xpath("/html/body/ul/li/a/text()")
print("Test1",result1)
### Test2 只拿ul中三个超链接中的第一个
result2=tree.xpath("/html/body/ul/li[1]/a/text()")#注意起始计数是从1开始的，从这里可以看出来!!!!一定要注意,[]表示索引
print("Test2",result2)
### Test3 拿到href的值为dapao的中文
result3=tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")#注意这里只有一个等号
print("Test3",result3)
### Test4 拿到大炮的href值
result4=tree.xpath("/html/body/ol/li/a/@href")# 这里不需要加text()
print("Test4",result4)
### Test5 对ol下的所有li进行遍历，再来进行筛选
print("Test5")
ol_li_list=tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    result5=li.xpath("./a/text()")#./表示的是当前的位置
    print(result5)
    result5=li.xpath("./a/@href")
    print(result5)