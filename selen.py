#!/bin/usr/python3
# Using Chrome version 112 with ChromeDriver 112.0.5615.49

# import all the necessary modules and packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    result = ("PRODUCT UNAVAILABLE")
    print(result)
else:
    result = ("IN STOCK")
    print(result)
    
# Create the email message
msg = MIMEMultipart()
msg['From'] = 'User@gmail.com'
msg['To'] = 'User@gmail.com'
msg['Subject'] = result

# Add the scraped result to the email message
body = str(result)
msg.attach(MIMEText(body, str))

# Set up the SMTP server and send the email.
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'User@gmail.com'
smtp_password = 'app-password-here'  # If using gmail, need to use App passwords to retrieve this.
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)
smtp_connection.sendmail(msg['From'], msg['To'], msg.as_string())
smtp_connection.quit()

#print(driver.page_source)
driver.quit()
