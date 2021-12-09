
'''
#first program python with selenium webdriver
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("https://www.facebook.com/")
print(driver.title)
print(driver.current_url)
driver.close()

#
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("http://demo.automationtesting.in/Register.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[1]/a").click()
time.sleep(5)
driver.close()

#navigators commonds...
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("https://accounts.google.com/b/0/AddMailService")
print(driver.title)
print(driver.current_url)
driver.get("http://demo.automationtesting.in/Register.html")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)
driver.quit()


#conditional commands....
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("https://www.facebook.com/")
print(driver.title)
user_ele=driver.find_element_by_id("email")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele=driver.find_element_by_name("pass")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("syed arifullah")
pwd_ele.send_keys("11721a0122")

driver.find_element_by_name("login").click()
# driver.close()


# implicity...

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("http://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10)
assert "welcome mercury tours,"in driver.title
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()


a=["arif",'a','bc','hsbbjkxwxj',"anil","Narendra","viswanath"]
#op=["htan","awsi","vardnera","nlinafira"]

str=""
for i in a:
    for j in i:
        str=j+ str
print(str)
b=[]
c=0
for i in a:
    d=c+len(i)
    # print(d)
    b.append(str[c:d])
    c=d
print(b)
'''

# waits
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
assert "welcome mercury tour"in driver.title
driver.find_element_by_id("email").send_keys("mercury")
driver.find_element_by_id("pass").send_keys("mercury")
driver.find_element_by_name("login").click()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("")

from sele











