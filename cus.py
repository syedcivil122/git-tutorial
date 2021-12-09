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