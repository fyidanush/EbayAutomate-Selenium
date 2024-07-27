
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time
chrome_driver_path = "C:\\Users\\Dhanush M\\Downloads\\chromedriver-win64\\chromedriver.exe"

options = Options()
options.add_argument("--start-maximized")

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.ebay.com/")
search_box = driver.find_element(By.ID, "gh-ac")
search_box.send_keys("laptop")
search_box.submit()

time.sleep(3) 

first_result = driver.find_element(By.XPATH, '//*[@id="item1af5f2da46"]/div/div[2]/a/div/span')
first_result.click()
driver.switch_to.window(driver.window_handles[1])

time.sleep(3)

add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="atcBtn_btn_1"]')
add_to_cart_button.click()

time.sleep(3) 

driver.quit()
