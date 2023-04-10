# selenium-scraper

## Python web scraper using Selenium and later BeautifulSoup.

* Requirements: python 3.8.10
* Chrome version 112 with ChromeDriver 112.0.5615.49

The essence of this scraper is to allow the program to:
- dismiss the cookie popup
- click on an "add to cart" button
- Check if product is in stock by looking for the out of stock signifiers. ( this website uses *** )

To set this scraper script on a schedule, you can use cron jobs / schedulers.
  - Open up the crotab file by typing in terminal ( crontab -e )
  - Add the following code to the bottom of the file
  -   0 9,21 * * * /path/to/python /path/to/your/script.py
  - That runs the script at 0 minutes, at 9am & 9pm, any day, any month, any day of week.
