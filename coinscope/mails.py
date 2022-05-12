from curses.ascii import EM
from distutils.log import error
from re import sub
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import sys
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

def webmail_login_cpanel(email, password):
    #Open firefox
    s=Service("/home/dev/personalProjects/upwork/wolf/geckodriver")
    #set headless
    options = Options()
    options.headless = False
    browser = webdriver.Firefox(service=s, options=options)#
    browser.get("https://vedroy.xyz:2096/")
    try:
        print("Inputing login credentials")
        email = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user']"))).send_keys(email)
        password = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='pass']"))).send_keys(password)
        time.sleep(10)
    except:
        print("Failed... Repeating loop")
        exit()
    time.sleep(1)
    try:
        print("Clicking login button")
        login = browser.find_element_by_id("login_submit").click() 
    except:
        print("Failed... Repeating loop")
        exit()       
    time.sleep(3)
    try:
        print("Click open on roundcube landing page")
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='launchActiveButton']"))).click()    
    except:
        print("Failed... Repeating loop")
        exit()
    try:
        print("Click refresh")
        time.sleep(30)
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='rcmbtn111']"))).click()      
    except:
        print("Failed... ending loop")
        exit()        
    try:
        print("Getting latest email")
        latest_email = browser.find_elements(By.CLASS_NAME, "message.unread")[0].get_attribute("innerHTML")
        print(latest_email)
    except:
        print("Failed to get latest... Repeating loop, waiting 30 seconds before retrying and exiting")
        time.sleep(30)
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='rcmbtn111']"))).click()
        latest_email = browser.find_element_by_id("rcmrowMQ").text
        print(latest_email)
        return latest_email
    return latest_email    

if __name__ == '__main__':
    webmail_login_cpanel("cidoFirst@vedroy.xyz", "to&nXZ;*Lzne")    