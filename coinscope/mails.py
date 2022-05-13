from multiprocessing.connection import wait
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
from tables import restrict_flavors


from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

def webmail_login_cpanel(email, password):
    #Open firefox
    s=Service("/home/dev/personalProjects/upwork/wolf/geckodriver")
    #set headless
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(service=s, options=options)
    browser.get("https://vedroy.xyz:2096/")
    unregistered  = open("unregistered.json", "w+")
    try:
        email = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user']"))).send_keys(email)
        password = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='pass']"))).send_keys(password)
        login = browser.find_element(By.ID, "login_submit").click() 
        WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.ID, "activeClientLogoContainer"))).click()     
        latest_email = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/table[2]/tbody/tr[1]/td[2]/span[3]/a/span").get_attribute("innerHTML")
        print(latest_email.split(" ")[0])
        if len(latest_email) == 0:
            time.sleep(4)
            browser.refresh()
            latest_email = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/table[2]/tbody/tr[1]/td[2]/span[3]/a/span").get_attribute("innerHTML")
            print(latest_email.split(" ")[0])

        return latest_email.split(" ")[0]

    except UnexpectedAlertPresentException:
        try:
            print("unexepcted error occured")
            browser.refresh()   
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "activeClientLogoContainer"))).click()  
            latest_email = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/table[2]/tbody/tr[1]/td[2]/span[3]/a/span").get_attribute("innerHTML")
            print(latest_email)
            return latest_email
            
        except UnexpectedAlertPresentException:
            data = {
                    "email" : email,
                    "password" : password
                }
            pass 
    
    except NoSuchElementException:
        return email

    except WebDriverException:
        try:
            time.sleep(2)
            browser.refresh()
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "activeClientLogoContainer"))).click()  
            latest_email = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/table[2]/tbody/tr[1]/td[2]/span[3]/a/span").get_attribute("innerHTML")
            print(latest_email)
            return latest_email

        except TimeoutException:
            print(
                ("time out fetching email")
            )
if __name__ == '__main__':
    webmail_login_cpanel("marywoods7d6@vedroy.xyz", "=i6v_^F621#aB!")    