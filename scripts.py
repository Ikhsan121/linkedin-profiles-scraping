import csv
import parameters
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from parsel import Selector


# Creating a webdriver instance
chrome_driver_path = Service("C:\Development\chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)
# This instance will be used to log into LinkedIn
driver.get("https://linkedin.com/uas/login")



# waiting for the page to load
time.sleep(1)
# Login to your account
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(parameters.linkedin_username)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(parameters.linkedin_password)
password_field.send_keys(Keys.ENTER)




driver.get('https:www.google.com')
time.sleep(3)

search_query = driver.find_element(By.NAME, 'q')
search_query.send_keys(parameters.search_query)
time.sleep(0.5)

search_query.send_keys(Keys.RETURN)
time.sleep(3)

linkedin_urls = driver.find_elements(By.CLASS_NAME, 'yuRUbf')
linkedin_urls = [url.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for url in linkedin_urls]
time.sleep(0.5)

#create list
profile_links = []
names = []
job_titles = []
# For loop to iterate over each URL in the list
for linkedin_url in linkedin_urls:

   # get the profile URL
   driver.get(linkedin_url)

   # add a 5 second pause loading each URL
   time.sleep(5)

   # assigning the source code for the webpage to variable sel
   sel = Selector(text=driver.page_source)

   name = sel.xpath('//h1/text()').extract_first()
   job_title = sel.xpath('//div[contains(@class,"text-body-medium")]/text()').extract_first()
   linkedin_url = driver.current_url
   if job_title:
      job_title = job_title.strip()

   if name:
      name = name.strip()


   print(f"name: {name}")
   print(f"job title: {job_title}")
   print(f"url: {linkedin_url}")
   print("**************")

# terminates the application
driver.quit()































