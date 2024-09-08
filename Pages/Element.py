from .BasePage import BasePage
import re
from selenium.webdriver.common.by import By

class Element(BasePage):
    btn_find_insure = (By.XPATH, '//*[@id="root"]/div[1]/div/div/div[8]/button')
    btn_customer_service = (By.XPATH, '//*[@id="root"]/div[1]/div/div/button')
    btn_agree = (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div[2]/div/button[1]')
    btn_destination = (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div/button')
    btn_nation_1 = (By.XPATH, '//*[@id="BottomSheetContainer"]/div/div/div[2]/div/div[1]/div[2]/button[1]')
    btn_confirm = (By.XPATH, '//*[@id="BottomSheetContainer"]/div/div/div[2]/div/div[2]/button')
    btn_period = (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/button')
    btn_user = (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[3]/div[2]/button')
    btn_kind= (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[4]/div[2]/button')
    btn_1day = (By.XPATH, '//*[contains(title(),"1일")]')
    btn_2day = (By.XPATH, '//*[contains(title(),"2일")]')
    btn_next = (By.XPATH, '//*[@id="BottomSheetContainer"]/div/div/div[2]/div[3]/button')

    destination_data = (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div/button/span[1]')

    img_inter = (By.XPATH, '//*[@id="root"]/div[1]/div/div/div[1]/div/div/img')
    interpark_img_src = "https://static.kakaoinsure.com/images/icons/TRP2312001_TRP301.png"

    text_notice = (By.XPATH, '//*[contains(text(),"꼭 확인하세요!")]')
    text_move_to_kakao = (By.XPATH, '//*[@id="root"]/div/div[2]/h2/text()[1]')
    text_conditions = (By.XPATH, '//*[contains(text(),"단체여행보험 가입 규약")]')
    text_where = (By.XPATH, '//*[contains(text(),"여행지를 알려주세요")]')
    text_period = (By.XPATH, '//*[@id="BottomSheetContainer"]/div/div/div[1]/strong')
    text_period_edit = (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/h3')
    text_start_day = (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div/button/div/p')
    text_last_day = (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div/button/div/p')
    text_enter_subscriber = (By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[3]/div[1]/div/h3')
