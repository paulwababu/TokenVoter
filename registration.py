from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import selenium
import time
import base64
from anticaptchaofficial.imagecaptcha import *

from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

def Register(credentials):
    
    if len(credentials) == 0:
        pass
    try:
        driver = uc.Chrome()
        userName = credentials.split(":")[0].split("@")[0]
        email    = credentials.split(":")[0]
        password = credentials.split(":")[1]
        print(userName, email, password)
        driver.get("https://coinsniper.net/register")
        WebDriverWait(driver, 5).until(Ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/footer/button"))).click()
        time.sleep(1)
        GetCaptcha(driver)
        WebDriverWait(driver, 5).until(Ec.presence_of_element_located((By.NAME, "name"))).send_keys(userName)
        WebDriverWait(driver, 5).until(Ec.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        time.sleep(1)
        WebDriverWait(driver, 5).until(Ec.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        time.sleep(1)
        WebDriverWait(driver, 5).until(Ec.presence_of_element_located((By.NAME, "password_confirmation"))).send_keys(password)
        WebDriverWait(driver, 5).until(Ec.presence_of_element_located((By.XPATH, "/html/body/section[4]/div/div/div/div/form/div[7]/div/input"))).click()
        time.sleep(1)
    except WebDriverException:
        pass

    except TimeoutException:
        pass

def CaptchaSolver():
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key("c1d3c7f98ad302af04e6635e9f84360a")
    captchaText = solver.solve_and_return_solution("captcha.jpeg")
    if captchaText != 0:
        print(captchaText)
        return captchaText
    else:
        return 1

def GetCaptcha(driver):
    driver.switch_to.frame(WebDriverWait(driver, 2).until(Ec.presence_of_element_located((By.ID, "mtcaptcha-iframe-1"))))
    time.sleep(5)
    imageB64 = driver.execute_script(
        """
        var elmt = arguments[0];
        var canv = document.createElement("canvas");
        canv.width = 300; canv.height = 80;
        canv.getContext('2d').drawImage(elmt, 0, 0);
        return canv.toDataURL('image/jpeg').substring(22);
        """, driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/img"))
    with open(r"captcha.jpeg", "wb") as image:
        image.write(base64.b64decode(imageB64))

    captchaText = CaptchaSolver()
    if captchaText == 1:
        print("[*] captcha not solver:")

    driver.find_element(By.ID, "mtcap-inputtext-1").send_keys(captchaText)
    driver.switch_to.default_content()


def main():
    with open("credentials.txt") as credentials:
        for item in credentials.readlines():
            Register(item)

main()