from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("https://www.edreams.in/")

radio=driver.find_element_by_xpath('//span[text()="One way "]')
radio.click()

check_box=driver.find_element_by_xpath('//div[text()="Direct flights only"]')
check_box.click()

hotels=driver.find_element_by_xpath('//div/span[2][text()="Hotels"]')
hotels.click()

rooms=driver.find_element_by_name("no_rooms")
rooms






