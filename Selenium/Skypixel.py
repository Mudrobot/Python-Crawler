from selenium.webdriver import Edge
import time
from selenium.webdriver.common.action_chains import ActionChains

'''
def get_track(distance):
	track = []
	current = 0
	mid = distance * 3 / 4
	t = 0.2
	v = 0
	while current < distance:
		if current < mid:
			a = 2
		else:
			a = -3
		v0 = v
		v = v0 + a * t
		move = v0 * t + 1 / 2 * a * t * t
		current += move
		track.append(round(move))
	return track
tracks=get_track(258)
'''
tracks=[128,64,32,16,8,4,4,2]
browser=Edge()
loginurl="https://www.skypixel.com/login?redirect=%2F"
browser.get(loginurl)
script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
browser.execute_script(script)#  这种修改该属性值的办法只在当前页面有效，当浏览器打开新标签或新窗口时需要重新执行改变navigator.webdriver值的JavaScript代码。
time.sleep(1)
user=browser.find_element_by_xpath('//*[@id="username"]')
user.click()
user.send_keys("XXXXXXX")
password=browser.find_element_by_xpath('//*[@id="password"]')
password.click()
password.send_keys("XXXXXX")
print("Already Done!")

button=browser.find_element_by_xpath('//*[@id="nc_1_n1z"]')
#创建一个动作
action=ActionChains(browser)#实例化一个action对象
action.click_and_hold(button).perform()
for track in tracks:
    #action.reset_actions()#清除当前动作
    action.move_by_offset(track, 0).perform()  # 移动滑块
    time.sleep(0.5)
#action.reset_actions()#清除当前动作链
action.release().perform()  # 移动滑块
