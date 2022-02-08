'''
from selenium import webdriver
import time

driver=webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get('https://www.facebook.com/')
print(driver.title)

driver.find_element_by_name("email").send_keys("syed")
driver.find_element_by_id("pass").send_keys("9703850562")
driver.find_element_by_name('login').click()

driver.close()
'''

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\User\Downloads\\ChromeSetup (1).exe")
driver.get("https://demo.guru99.com/test/newtours/")
print(driver.title)









