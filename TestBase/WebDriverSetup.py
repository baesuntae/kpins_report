import unittest
from selenium import webdriver
from time import *
from Config import config
from selenium.webdriver.chrome.options import Options


class WebDriverSetup(unittest.TestCase):

    def setUp(self) -> None:
        # ChromeOptions 객체 생성
        chrome_options = Options()
        # 모바일 디바이스 에뮬레이션 설정
        mobile_emulation = {
            "deviceName": "iPhone 14 Pro Max"
        }
        # 옵션에 모바일 에뮬레이션 추가
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # WebDriver 객체 생성
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        url = config.url_info[config.EnvVar.getInstance().test_url]
        print(url)

        self.driver.get(url=url)



    def tearDown(self) -> None:
        self.driver.quit()
        sleep(5)



if __name__ == '__main__':
    unittest.main()