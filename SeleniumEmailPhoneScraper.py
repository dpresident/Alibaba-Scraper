from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Chrome
import re #regular expressions, are imported from python directly

#browser = webdriver.Chrome('/home/daniel/Documents/chromedriver')
browser = webdriver.Firefox()
#browser.get('https://www.alibaba.com/product-detail/Portable-Small-USB-Travel-LED-Makeup_60830030133.html?spm=a2700.details.maylikever.2.1fb53cc2uSVPvx')
#browser.get('https://selenium.dev/documentation/en/')
browser.maximize_window()
browser.get('https://www.aeropuertomadrid-barajas.com/eng/madrid-barajas-airport-info.htm')
doc = browser.page_source #page source, we are going to look into it
emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc) #search for emails using regular expresions
Phones = re.findall(r'[(][\D]{1}[\d]{2}[)][\D]{1}[\d]{3}[\D]{1}[\d]{3}[\D]{1}[\d]{3}', doc) #phone numbers, format: (+34) 91 321 10 00.

for email in emails: #for an element inside the document 'doc', search for sub elements
    print(email)

for phone in Phones:
    print(phone)
