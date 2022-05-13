from multiprocessing.connection import wait
from re import sub
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import sys
from selenium.webdriver.support import expected_conditions as Ec
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from tables import restrict_flavors
import random
import mails
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

#Open firefox
def twitter_sign_up():
    s=Service("/home/tinka/Desktop/angular tutorials/tiktodv3/TokenVoter/coinscope/geckodriver")
    #set headless
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(service=s, options=options)
    browser.get("https://twitter.com/i/flow/signup")
    #user email instead
    try:
        email = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Sign up with phone or email')]"))).click()
        time.sleep(2)
        email = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Use email instead']"))).click()
        time.sleep(2)
    except:
        print("Use Email Not Found...Exiting now")
        exit()
    #get credentials from json
    data = open("test_register.json", "r")
    emailJson = json.loads(data.read())
    for credentials in emailJson:
        email = credentials["email"] + '@vedroy.xyz'
        password = credentials["password"]
        userPassword = f"{email}:{password}"
        username = userPassword.split(":")[0].split("@")[0]
        passcode = userPassword.split(":")[1]
        emcode = userPassword.split(":")[0]
    #enter username
    try:
        signup_username = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))).send_keys(username)
        signup_email = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))).send_keys(email)
        time.sleep(2)
        Select(browser.find_element(By.ID, "SELECTOR_1")).select_by_index(random.randint(1, 12))
        Select(browser.find_element(By.ID, "SELECTOR_2")).select_by_index(random.randint(1, 31))
        Select(browser.find_element(By.ID, "SELECTOR_3")).select_by_index(random.randint(25, 50))
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div").click()
        code = mails.webmail_login_cpanel(email, password)

        if code.isdigit() == False:
            time.sleep(5)
            code = mails.webmail_login_cpanel(email, password)


        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").send_keys(code)
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()
        WebDriverWait(browser, 5).until(Ec.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        time.sleep(5)
        browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()
        print(f"[*] Created {email}")
        # function to add to JSON
        def write_json(new_data, filename='twitter_registered.json'):
            with open(filename,'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                file_data["credentials_json"].append(new_data)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent = 4)
        
            # python object to be appended
        y = {"email":email,
            "password": password
            }
            
        write_json(y)
        browser.close()
    except:
        print("Username Not Found...Exiting now")
        exit()    

twitter_sign_up()
