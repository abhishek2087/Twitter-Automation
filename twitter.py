from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Login process
driver.get('https://twitter.com/login')
username = os.environ.get('TWIT_USER')
password = os.environ.get('TWIT_PASS')

search = driver.find_element_by_name('session[username_or_email]')
search.send_keys(username)
time.sleep(1)
search = driver.find_element_by_name('session[password]')
search.send_keys(password)
time.sleep(1)
search.send_keys(Keys.RETURN)


#Tweeting process
msg_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'

time.sleep(1)

driver.find_element_by_xpath(msg_xpath).send_keys('Hi! this tweet is posted using Python Selenium')
time.sleep(0.5)
driver.find_element_by_xpath(tweet_xpath).click()

time.sleep(1)

#logging out
account = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]')
account.click()
time.sleep(1)
log_out = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]')
log_out.click()
time.sleep(1)
final_click = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/span/span')
final_click.click()
