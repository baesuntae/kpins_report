from TestBase.WebDriverSetup import WebDriverSetup
from selenium.common.exceptions import NoSuchElementException
from Pages.BasePage import BasePage
from Pages.Element import Element
from Config import config
import time
from datetime import datetime


class Scenario(WebDriverSetup):

    def test_001(self):
        el = Element(self.driver)

        try:
            # 로그인 과정
            time.sleep(2)
            #driver.find_element(By.XPATH, '//*[@id="gnb-header"]/nav/div[2]/a[1]').click()
            el.click(el.btn_mypage)
            time.sleep(1)

            time.sleep(1)
            # driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/form/div[1]/div/div/div/input').send_keys(config.user[0])
            # driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/form/div[2]/div/div/input').send_keys(config.user[1])
            # time.sleep(1)
            # driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/form/div[3]/button').click()
            time.sleep(4)

        except NoSuchElementException:
            print("No Such Element Exception")
            self.assertTrue(False)
        except AssertionError:
            print("Assertion Error Occured")
            self.assertTrue(False)
        except:
            print("Unknown error")
            self.assertTrue(False)
