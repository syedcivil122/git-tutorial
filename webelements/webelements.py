import select
import time


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")

flight_booking="https://www.edreams.in/"

driver.get(flight_booking)
driver.maximize_window()
print(driver.title)

'''

search=driver.find_element_by_id("search_query_top")
search.click()
search.send_keys("model dress")
time.sleep(4)

search.send_keys(Keys.BACK_SPACE)
time.sleep(4)
search.clear()

submit=driver.find_element_by_name("submit_search")
submit.click()


#radio button
radio=driver.find_element_by_xpath('//span[text()="Multi-city"]')
radio.click()


check=driver.find_element_by_xpath('//div[text()="Direct flights only"]')
check.click()


covid=driver.find_element(By.XPATH,'//div[@data-card="covid"]')
covid.click()
'''
hotels=driver.find_element_by_xpath('//div/span[2][text()="Hotels"]')
hotels.click()
time.sleep(3)

rooms=driver.find_element_by_name("no_rooms")
Dropdown_1=Select(rooms)
Dropdown_1.select_by_index('1')
time.sleep(3)

adults=driver.find_element(By.NAME,'//select[@name="group_adults"]')
Dropdown_2=Select(adults)
Dropdown_2.select_by_value('3')
time.sleep(3)

children=driver.find_element(By.NAME,'//select[@name="group_children"]')
Dropdown_3=Select(children)
Dropdown_3.select_by_visible_text('4')
time.sleep(3)





