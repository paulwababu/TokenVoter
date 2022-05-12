from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as Ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

import undetected_chromedriver as uc
from fake_useragent import UserAgent
import time, os, zipfile

class Gleam:
         
   
    def __init__(self, port, ip, username, password):

        self.proxyPort       = port
        self.proxyIp         = ip
        self.proxyUserName   = username
        self.proxyPassword   = password

        self.manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }  """

        self.background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                  singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                  },
                  bypassList: ["localhost"]
                }
              };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }
        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );""" % (self.proxyIp, self.proxyPort, self.proxyUserName, self.proxyPassword)



    def ChromeSetUp(self, use_proxy=False, user_agent=None):
        path = os.path.dirname(os.path.abspath(__file__))
        chromeOptions = Options()
        if use_proxy:
            pluginFile = "proxyAuthPlugin.zip"

            with zipfile.ZipFile(pluginFile, "w") as zipFile:
                zipFile.writestr("manifest.json", self.manifest_json)
                zipFile.writestr("background.js", self.background_js)
            chromeOptions.add_extension(pluginFile)

        if user_agent:
            chromeOptions.add_argument("--user-agent=%s" % user_agent)
        #chromeOptions.add_argument("--incognito")
        chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
        chromeOptions.add_experimental_option('useAutomationExtension', False)
        chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
        service = Service("/home/dev/personalProjects/upwork/Audrey/GleamBot/driver/chromedriver")
        chromeOptions.add_argument('--no-sandbox')
        driver = webdriver.Chrome(service=service, options=chromeOptions)
        #driver = uc.Chrome()
        return driver

if __name__ == "__main__":
    gleam = Gleam(12323,"51.161.196.188",  "abdul9999", "Asdfqwer1")
    gleam.ChromeSetUp(use_proxy=True, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")