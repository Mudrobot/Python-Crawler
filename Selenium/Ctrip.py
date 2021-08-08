from selenium.webdriver import Edge
import time
from selenium.webdriver.common.action_chains import ActionChains
url='https://passport.ctrip.com/user/reg/home'
browser=Edge()
browser.get(url)
time.sleep(0.5)
browser.find_element_by_css_selector('#agr_pop > div.pop_footer > a.reg_btn.reg_agree').click()
time.sleep(0.5)
button=browser.find_element_by_css_selector('#slideCode > div.cpt-drop-box > div.cpt-drop-btn')
action=ActionChains(browser)
action.click_and_hold(button).perform()
action.move_by_offset(268, 0).perform()
action.release()