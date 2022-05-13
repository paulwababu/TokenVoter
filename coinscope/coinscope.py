from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium import webdriver
from queue import Queue
from threading import Thread
import undetected_chromedriver as uc
import time, tqdm, json
import random

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException 

import mails
from configs import Gleam
class Coinscope:
    def __init__(self):
        pass

    def RegisterTwitter(driver, queue):
        while not queue.empty():
            user = 0
            credentials = queue.get_nowait()
            if len(credentials) == 0:
                pass
            try:
                gleam = Gleam(12323, "51.161.196.188",  "abdul9999", "Asdfqwer1")
                driver = gleam.ChromeSetUp(use_proxy=True, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
                userName = credentials.split(":")[0].split("@")[0]
                email    = credentials.split(":")[0]
                password = credentials.split(":")[1]
                unregistered = []
                driver.get("https://twitter.com/signup")
                WebDriverWait(driver, 120).until(Ec.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]"))).click()
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]").click()
                driver.find_element(By.NAME, "name").send_keys(userName)
                driver.find_element(By.NAME, "email").send_keys(email)
                Select(driver.find_element(By.ID, "SELECTOR_1")).select_by_index(random.randint(1, 12))
                Select(driver.find_element(By.ID, "SELECTOR_2")).select_by_index(random.randint(1, 31))
                Select(driver.find_element(By.ID, "SELECTOR_3")).select_by_index(random.randint(25, 50))
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div").click()
                code = mails.webmail_login_cpanel(email, password)

                if code.isdigit() == False:
                    time.sleep(5)
                    code = mails.webmail_login_cpanel(email, password)


                time.sleep(1)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").send_keys(code)
                time.sleep(1)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()
                WebDriverWait(driver, 5).until(Ec.presence_of_element_located((By.NAME, "password"))).send_keys(password)
                time.sleep(5)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()
                time.sleep(15)
                print(f"[*] Created {email}")
                driver.close()
            
            except StaleElementReferenceException as error:
                pass
        
            except NoSuchElementException as error:
                data = {
                    "email" : email,
                    "password" : password
                }
                unregistered.append(data)
                pass

            except TimeoutException:
                data = {
                    "email" : email,
                    "password" : password
                }
                unregistered.append(data)
                pass

            except AttributeError:
                data = {
                    "email" : email,
                    "password" : password
                }
                unregistered.append(data)
                pass

    def Voter(self, credentials):
        gleam = Gleam(12323, "51.161.196.188",  "abdul9999", "Asdfqwer1")
        driver = gleam.ChromeSetUp(use_proxy=True, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
        userName = credentials.split(":")[0].split("@")[0]
        email    = credentials.split(":")[0]
        password = credentials.split(":")[1]
        self.driver.get("https://www.coinscope.co/login")
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(Ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div/div/div[1]/form/ul/li[2]/button"))).click()
        currentWindow = self.driver.window_handles[0]
        time.sleep(5)
        windowAfter = self.driver.window_handles[1]
        self.driver.switch_to.window(windowAfter)
        time.sleep(5)
        self.driver.find_element(By.ID, "username_or_email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "allow").submit()
        WebDriverWait(self.driver, 5).until(Ec.presence_of_element_located((By.ID, "challenge_response"))).send_keys("0712075893")
        WebDriverWait(self.driver, 5).until(Ec.presence_of_element_located((By.ID, "email_challenge_submit"))).submit()
        time.sleep(5)
        self.driver.switch_to.window(currentWindow)
        time.sleep(5)
        self.driver.get("https://www.coinscope.co/coin/gwolf")
        WebDriverWait(self.driver, 5).until(Ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[1]/div/div[3]/div[1]/div[2]/button[1]"))).submit()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div[3]/button").submit()
        time.sleep(10)
        self.driver.close()


def AddEmails(queue):
    data = open("credetials.json", "r")
    emailJson = json.loads(data.read())
    for credentials in emailJson:
        email = credentials["email"] + '@vedroy.xyz'
        password = credentials["password"]
        userPassword = f"{email}:{password}"
        if queue.full() != True:
            queue.put(userPassword)

def CreateThreads():
    queue = Queue()
    AddEmails(queue=queue)
    coinscope = Coinscope()
    for thread in range(0, 3):
        worker = Thread(target=coinscope.RegisterTwitter, args=(queue, ))
        worker.start()
    queue.join()
    proc = tqdm.tqdm(total=queue.qsize())


if __name__ == "__main__":
    #coinscope = Coinscope(driver)
    #coinscope.Voter("asidohsidney254@gmail.com:Asidoh254")
    CreateThreads()