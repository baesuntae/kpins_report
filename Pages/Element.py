from .BasePage import BasePage
import re
from selenium.webdriver.common.by import By

class Element(BasePage):
    btn_mypage = (By.XPATH, '//*[@id="gnb-header"]/nav/div[2]/a[1]')