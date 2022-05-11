from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from sympy import not_empty_in
import undetected_chromedriver as uc
import selenium
import time
from configs import Gleam

def Coinsniper(credentials, number):
    gleam = Gleam("geo.iproyal.com", 12323, "abdul9999", "Asdfqwer1")
    driver = gleam.ChromeSetUp(use_proxy=True, user_agent=None)
    driver.get("https://www.coinsniper.net/login")
    time.sleep(10)
    email = credentials.split(":")[0]
    password = credentials.split(":")[1]
    driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/footer/button").click()
    WebDriverWait(driver, 5).unitl((Ec.presence_of_element_located(By.NAME, "email"))).send_keys(email)
    time.sleep()
    WebDriverWait(driver, 5).unitl((Ec.presence_of_element_located(By.NAME, "password"))).send_keys(password)
    WebDriverWait(driver, 5).until((Ec.presence_of_element_located(By.XPATH, "/html/body/section[4]/div/div/div/div/form/div[4]/div/input"))).submit()
    driver.get("https://www.coinsniper.net/coin/31029")
    WebDriverWait(driver, 5).until((Ec.presence_of_element_located(By.XPATH, "/html/body/section[4]/div[3]/div/div[2]/div[2]/div[1]/div[2]/button"))).click()
    driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/section[4]/div[4]/div[2]/section/div/form/div/div[1]/div/div/iframe"))
    driver.find_element(By.ID, "checkbox").click()
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "/html/body/section[4]/div[4]/div[2]/section/div/form/div/div[2]/button").click()
    driver.find_element(By.XPATH, "/html/body/section[4]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/div[3]/span").click()
    print(f"[*] Vote {number} for {email}")
    time.sleep(5)
