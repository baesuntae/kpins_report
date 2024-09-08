from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    """""공통 동작 정보"""""
    #클릭 함수
    def click(self, by_locator): # 클릭 함수
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        #by_locator.click()

    # 페이지 마지막까지 스크롤
    def scrollToEnd(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 특정 엘리먼트까지 스크롤
    def scrollToElement(self, by_locator):
        some_tag = self.driver.find_element(by_locator[0], by_locator[1])
        action = ActionChains(self.driver)
        action.move_to_element(some_tag).perform()

    # def findElement(self, by_locator):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # 특정 엘리먼트까지 나올때가지 대기
    def waitfor_element(self, by_locator, max_wait_time):
        try:
            WebDriverWait(self.driver, max_wait_time).until(EC.visibility_of_element_located(by_locator))
            element = True
        except:
            element = False
        return bool(element)

    # 텍스트 가져오는 함수
    def get_text(self, by_locator):
        get_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        return get_text

    # 특정 엘리먼트 존재여부를 반환하는 함수
    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(by_locator))
        except:
            element = False
        return bool(element)
