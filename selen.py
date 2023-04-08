#!/bin/usr/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
#options.headless = True
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.twinbusch.com/product_info.php?products_id=8")

# add cookie accept button
button = driver.find_element(By.ID, "cookieChoiceDismiss")
button.click()

time.sleep(5)

button = driver.find_element(By.CLASS_NAME, "addtobasket_button")
button.click()

time.sleep(5)



print(driver.page_source)
#driver.quit()
