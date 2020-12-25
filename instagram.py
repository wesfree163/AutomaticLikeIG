#!/usr/bin/env Python3
# from pywinauto import Application
from time import sleep
# import json
# import os
# import autoit
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from pywinauto import Application
import random


# Variables
driver = ""


def launch_inst():
    global driver
    print("Opening instagram")

    # Chrome browser options for emulation
    # mobile_emulation = {"deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #                     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    # opts = webdriver.ChromeOptions()
    # opts.add_argument("window-size=1,765")
    # opts.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")


    # Opens Instagram
    main_url = "https://www.instagram.com"
    driver.get(main_url)
    sleep(10)
    

def login():
    # Logs into instagram
    print("Logging into Instagram")
    driver.find_element_by_name("username").click()
    username = driver.find_element_by_name("username")
    username.send_keys("", Keys.ENTER)
    # password.send_keys(Keys.RETURN) for Mac users
    sleep(3)
    # driver.find_element_by_xpath("//a[contains(text(),'Not now')]").click()

def remove_popups():
    print("Removing any popups")
    try:
        driver.find_element_by_xpath("//a[contains(text(),'Not Now')]").click()
    except:
        try:
            driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        except:
            try:
                driver.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
            except:
                pass

def likes():
    x = random.uniform(12.1518, 21.2427)
    driver.get("https://www.instagram.com/explore/tags/music/")
    sleep(x)
    remove_popups()

    sleep(x)
    driver.find_element_by_class_name("_9AhH0").click()

    # 1
    sleep(x)
    like = driver.find_element_by_class_name('fr66n')
    soup = bs(like.get_attribute('innerHTML'),'html.parser')
    if soup.find('svg')['aria-label'] == 'Like':
      like.click()
    sleep(x)
    driver.find_element_by_class_name("_65Bje").click()
    

    sleep(36)
    remove_popups()
   


launch_inst()
login()

remove_popups()
sleep(15)
remove_popups()
sleep(15)
remove_popups()
sleep(15)
remove_popups()
sleep(15)
remove_popups()

for y in range(36):
    likes()

    print("itr ")
    print(y)
    print(" complete")
    sleep(3600)
    