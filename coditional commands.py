from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:/Users/User/Downloads/chromedriver_win32/chromedriver")
driver.get=("https://www.facebook.com/")

user_ele=driver.find_element_by_name("username")
print(user_ele.is_enabled())
print(user_ele.is_displayed())

mob_ele=driver.find_element_by_name("mobile number")
print(mob_ele.is_displayed())
print(mob_ele.is_enabled())

emil_ele=driver.find_element_by_id("email")
print(emil_ele.is_displayed())
print(emil_ele.is_enabled())

pass_ele=driver.find_element_by_name("password")
print(pass_ele.is_displayed())
print(pass_ele.is_enabled())


user_ele.send_keys("arif")
mob_ele.send_keys("23232123")
emil_ele.send_keys("syedcivil122")
pass_ele.send_keys("111111")

