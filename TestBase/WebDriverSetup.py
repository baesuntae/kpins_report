import unittest
from selenium import webdriver
from time import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class WebDriverSetup(unittest.TestCase):

    def setUp(self) -> None:


        chrome_options = Options()
        mobile_emulation = {"deviceName": "iPhone X"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


        self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        url = "https://talk.kakaoinsure.com/partner/plan/FAA004?campaignCode=TRP2312001&dc=TRP301"
        self.driver.get(url=url)



    def tearDown(self) -> None:
        self.driver.quit()
        sleep(5)



if __name__ == '__main__':
    unittest.main()