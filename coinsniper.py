from matplotlib.pyplot import table
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import selenium
import time

def Browser():
    driver = uc.Chrome() #webdriver.Chrome("/home/dev/personalProjects/upwork/wolf/chromedriver")
    driver.get("https://www.coinsniper.net")
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/footer/button").click()
    time.sleep(2)
    #login
    driver.find_element(By.CLASS_NAME, "nav-burger").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/section[2]/div/ul[1]/li[2]/a").click()
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("ftudiosafrica@gmail.com")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("asidoh254")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/section[4]/div/div/div/div/form/div[4]/div/input").submit()
    time.sleep(5)
    driver.get("https://www.coinsniper.net/coin/31029")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/section[4]/div[3]/div/div[2]/div[2]/div[1]/div[2]/button").click()
    time.sleep(5)
    iframe = driver.find_element(By.XPATH, "/html/body/section[4]/div[4]/div[2]/section/div/form/div/div[1]/div/div/iframe")
    driver.switch_to.frame(iframe)
    driver.find_element(By.ID, "checkbox").click()
    time.sleep(2)
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "/html/body/section[4]/div[4]/div[2]/section/div/form/div/div[2]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/section[4]/div[3]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/div[3]/span").click()
    print("voted Wolf and added to watchlist")
    time.sleep(5)

Browser()