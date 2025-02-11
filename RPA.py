from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# from bs4 import BeautifulSoup
import time
import requests
import os
import math
import sys
import io

driver = webdriver.Chrome()

try :
    driver.get("https://eis4ce.cpall.co.th/bench")

    # Put Username & Password then Enter Login
    username_user = driver.find_element(By.XPATH, '/html/body/section/form/fieldset/div[1]/div/input')
    password_user = driver.find_element(By.XPATH, '/html/body/section/form/fieldset/div[2]/div/input')

    username_user.send_keys('arthit')
    password_user.send_keys('11111111')

    password_user.send_keys(Keys.RETURN)
    time.sleep(3)

    # Click Search
    search_button = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/ul/li[3]/a')
    search_button.click()
    time.sleep(1)

    # Click Special form
    spef_button = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/ul/li[3]/ul/li[2]/a')
    spef_button.click()
    time.sleep(3)

    # Choose Filter Clearsites SA
    CS_filter = Select(driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div[6]/form/div/div[1]/div[5]/div[2]/select'))
        # Get value From F12
    CS_filter.select_by_value('263')
    time.sleep(2)

    # Select Date start
    date_start = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div[6]/form/div/div[2]/div[2]/input[1]')
    date_start.send_keys('1/2/2568')
    time.sleep(2)

    # Select Date end
    date_end = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div[6]/form/div/div[2]/div[2]/input[2]')
    date_end.send_keys('10/2/2568')
    time.sleep(2)

    # ค้นหา <body> และคลิกเพื่อปิดปฏิทิน
    driver.find_element("tag name", "body").click()
    time.sleep(2)
    
    # Search
    search_button = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div[6]/form/div/div[6]/input[1]')
    search_button.click()
    time.sleep(2)

    # Export Button
    Export_button = driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div/div[1]/a/img')
    Export_button.click()
    time.sleep(2)

    speExport_button = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div[20]/div[3]/a[3]/div')
    speExport_button.click()
    time.sleep(2)

    # Choose Filter Clearsites SA
    CS_filter = Select(driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div[23]/div[2]/div[1]/div[1]/select'))
        # Get value From F12
    CS_filter.select_by_value('263')
    time.sleep(2)

    Export_button = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div[23]/div[2]/div[3]/div/a/input')
    Export_button.click()
    time.sleep(5)

finally:
    driver.quit()