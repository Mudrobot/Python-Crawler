# selenium框架实现登录小说网获取一部小说的操作
from selenium.webdriver import Edge
import time
browser = Edge()
browser.get('https://www.17k.com/')
login=browser.find_element_by_xpath('//*[@id="header_login_user"]/a[1]')
login.click()#点击这个东西
time.sleep(1)
frame=browser.find_element_by_xpath("/html/body/div[21]/div/div[1]/iframe")
browser.switch_to_frame(frame)#切换一下html，因为我们的登录界面是一个内嵌在主页面中的html
user=browser.find_element_by_xpath("/html/body/form/dl/dd[2]/input")
user.click()
user.send_keys("XXXXX")
password=browser.find_element_by_xpath("/html/body/form/dl/dd[3]/input")
password.click()
password.send_keys("XXXXXX")
browser.find_element_by_xpath("/html/body/form/dl/dd[5]/input").click()
#browser.quit()
time.sleep(1)
browser.switch_to_default_content()#将窗口切换回初始窗口，一般情况是不使用的
shelf=browser.find_element_by_xpath("/html/body/div[1]/div[2]/dl/dd[3]/div/a")
shelf.click()
#下面实现页面切换
#因为关的有点快所以这里加一个三秒的睡眠
time.sleep(3)
browser.switch_to_window(browser.window_handles[0])#切换回第一个窗口
time.sleep(3)
browser.close()#关掉第一个窗口