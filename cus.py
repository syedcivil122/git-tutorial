'''
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver')

driver.get('https://www.facebook.com/?nocaa=1')
driver.maximize_window()
driver.implicitly_wait(10)

ele = driver.find_element_by_id('email')
print(ele.is_displayed())
print(ele.is_enabled())
if ele.is_displayed():
 ele.send_keys('xxxx@gmail.com')

els = driver.find_element_by_id('pass')
els.send_keys('xxxxxxxxxxx')

driver.find_element_by_name('login').click()

print(driver.current_url)

driver.close()


from selenium import webdriver

driver=webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)

user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name('submit').click()

#implicity
from selenium import webdriver

driver=webdriver.Chrome("C:/Users/User/Downloads/chromedriver_win32/chromedriver")
driver.get("http://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10)
print(driver.title)

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("submit").click()


from selenium import webdriver

from selenium.webdriver.chrome.service import Service

s=Service("C:/Users/User/Downloads/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")


from selenium import webdriver

from selenium.webdriver.edge.service import Service

s=Service("C:/Users/User/Downloads/chromedriver_win32/chromedriver")

#initilize chrome
driver=webdriver.Chrome(service=s)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service("C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")

driver=webdriver.Chrome(service=s)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

time.sleep(5)

'''
import time

from selenium import webdriver
#from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("---headless")

#s=Service("C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
#initialize chrome
#driver=webdriver.Chrome(service=s)
driver=webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("http://automationpractice.com/index.php")

print(driver.title)
time.sleep(5)
contact=driver.find_element_by_xpath("//*[@id='contact-link']/a")
contact.click()

#go back
driver.back()
time.sleep(5)

#go forward
driver.forward()
time.sleep(5)


#minimaize window
driver.minimize_window()
time.sleep(2)

#maximize window
driver.maximize_window()
time.sleep(2)


# refresh
driver.refresh()
time.sleep(5)

driver.close()
print("the page is closed successfully")





















