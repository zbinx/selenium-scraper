#!/bin/usr/python3
# Using Chrome version 112 with ChromeDriver 112.0.5615.49

# import all the necessary modules and packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# create the options variable to avoid errors & to add options like headless or window size.
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Do not use headless until you verify in real time the code is doing what you want it to do.
options.add_argument("--window-size=1920,1080")

# add the webdriver you downloaded into the root folder of project and call it using ./chromedriver
#driver = webdriver.Chrome("./chromedriver") 
# the code above is deprecated and replaced with code below.

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# The webpage you are scraping for step 1.
driver.get("https://www.twinbusch.com/product_info.php?products_id=8")

# Bypass the cookie popup message by clicking the accept or I understand button
button = driver.find_element(By.ID, "cookieChoiceDismiss")
button.click()

# time delay before next line of code
time.sleep(5) 

# Code to click the Add to Cart button
button = driver.find_element(By.CLASS_NAME, "addtobasket_button")
button.click()

time.sleep(5)

# create variable to store the html source code of page.
html = driver.page_source 

# Create if else statement to see if the *** signifier shows up indicating out of stock.
if '***' in html:
    print('PRODUCT UNAVAILABLE')
else:
    print('IN STOCK AND AVAILABLE')
    
#print(driver.page_source)
driver.quit()
