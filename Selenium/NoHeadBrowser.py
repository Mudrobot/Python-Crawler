from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select#处理下拉列表使用
import time
#进行无头浏览器参数配置——无头模式的抓取更快
path = "MicrosoftWebDriver.exe"
EDGE = {
            "browserName": "MicrosoftEdge",
            "version": "",
            "platform": "WINDOWS",
            # 关键是下面这个
            "ms:edgeOptions": {
                'extensions': [],
                'args': [
                    '--headless',
                    '--disable-gpu',
                    '--remote-debugging-port=9222',
                ]}
        }
# 把参数配置到浏览器中

browser= Edge(executable_path=path, capabilities=EDGE)



#===========================================
data=[]
databaseurl="https://www.endata.com.cn/BoxOffice/BO/Year/index.html"
browser.get(databaseurl)
#定位到下拉列表
sel_loc=browser.find_element_by_xpath('//*[@id="OptionDate"]')
#对元素进行包装，包装成下拉菜单
sel=Select(sel_loc)
#让浏览器进行调整选项
for i in range(len(sel.options)):
    sel.select_by_index(i)
    data.append(2021-i)
    time.sleep(2)
    movie_name=browser.find_elements_by_xpath('//*[@id="TableList"]/table/tbody/tr/td[2]/a/p')
    for namm in movie_name:
        data.append(namm.text)
for ele in data:
    print(ele)
#如何拿取加载过后的页面源代码：
html=browser.page_source
with open("PageSource.html","w",encoding="utf-8") as f:
    f.write(html)
browser.close()