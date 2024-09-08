from TestBase.WebDriverSetup import WebDriverSetup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Pages.Element import Element
from datetime import datetime
from Config import config
import time
import datetime



class Scenario(WebDriverSetup):
    def test_001(self):
        el = Element(self.driver)
        try:
            print("----start test_001----")
            # When: 1. 브라우저 > URL 입력란에 인터파크 해외여행자보험 주소 입력
            print("When: 1. 브라우저 > URL 입력란에 인터파크 해외여행자보험 주소 입력")
            el.waitfor_element(Element.btn_find_insure, 10)  # 페이지 실행 완료될때까지 대기
            img_element = self.driver.find_element(Element.img_inter[0],Element.img_inter[1]) # 기존 저장해 둔 협업사 정보 가져오기
            img_src = img_element.get_attribute('src') # 현재 페이지 협업사 정보
            # Then: 1. 최상단: 'INT X pay 손해보험' 표시됨
            print("Then: 1. 최상단: 'INT X pay 손해보험' 표시됨")
            self.assertEqual(img_src, el.interpark_img_src) # 기존 저장해 둔 협업사 정보와 현재 페이지 현업사 정보 일치여부 확인
            print("Step1 Pass")

            """Step 2. Desktop으로 진행 방법 확인 필요"""
            # # When: 2. 하단 [고객센터 >] 버튼 클릭
            # print("When: 2. 하단 [고객센터 >] 버튼 클릭")
            # el.waitfor_element(Element.btn_customer_service,10)
            # el.scrollToElement(Element.text_notice) # 고객센터 버튼 부분까지 스크롤
            # el.click(Element.btn_customer_service)
            # time.sleep(3)
            # text = el.get_text(Element.text_move_to_kakao)
            # # Then: 2. 무엇을 도와드릴까요? 페이지로 랜딩됨
            # print("Then: 2. 무엇을 도와드릴까요? 페이지로 랜딩됨")
            # text = el.get_text(Element.text_move_to_kakao)

            # When: 4. [내 보험료 알아보기] 버튼 클릭
            print("When: 04. [내 보험료 알아보기] 버튼 클릭")
            el.click(Element.btn_find_insure) # [내 보험료 알아보기] 버튼 클릭
            time.sleep(1)
            # Then: 4. 보험료 조회 페이지로 랜딩됨 + 단체여행보험 가입 규약 팝업됨
            print("Then: 4. 보험료 조회 페이지로 랜딩됨 + 단체여행보험 가입 규약 팝업됨")
            result4 = el.is_visible(Element.text_conditions) # 단체여행보험 가입 규약 팝업됨 출력 여부 확인
            self.assertTrue(result4)
            print("Step4 Pass")

            # When: 5, [동의할게요] 클릭
            print("When: 5, [동의할게요] 클릭")
            el.click(Element.btn_agree) # 규약 팝업 > [동의할게요] 버튼 클릭
            # Then: 5, 단체여행보험 가입 규약 팝업이 닫히고, 보험료 조회 페이지가 활성화 됨
            print("Then: 5, 단체여행보험 가입 규약 팝업이 닫히고, 보험료 조회 페이지가 활성화 됨")
            result5_1 = el.is_visible(Element.text_conditions) # 규약 팝업 여부
            result5_2 = el.is_visible(Element.btn_destination) # 보험료 조회 페이지 여부
            self.assertFalse(result5_1)
            self.assertTrue(result5_2)
            print("Step5 Pass")

            # When: 6. 여행지를 입력해 주세요 입력란 클릭
            print("When: 6. 여행지를 입력해 주세요 입력란 클릭")
            el.click(Element.btn_destination) # 여행지를 입력해주세요 입력란 클릭
            # Then: 6. 여행지 입력 바텀 시트가 출력됨
            print("Then: 6. 여행지 입력 바텀 시트가 출력됨")
            result6 = el.is_visible(Element.text_where) # 바텀시트 출력 여부
            self.assertTrue(result6)
            print("Step6 Pass")

            # When: 7. [일본] 선택 후 [확인] 버튼 클릭
            print("When: 7. [일본] 선택 후 [확인] 버튼 클릭")
            time.sleep(2)
            compare = el.get_text(Element.btn_nation_1) # 버튼 클릭 전 text get
            el.click(Element.btn_nation_1) # 첫번째 키워드 항목(일본) 클릭
            el.click(Element.btn_confirm) # [확인] 버튼 클릭
            # Then: 7. 바텀시트가 닫히고, 선택한 국가가 여행지 입력란에 입력됨
            print("Then: 7. 바텀시트가 닫히고, 선택한 국가가 여행지 입력란에 입력됨")
            result7 =el.get_text(Element.destination_data) # 여정 표시란 text get
            self.assertEqual(compare,result7) # 클릭한 text 와 출력된 text 비교
            print("Step7 Pass")

            # When: 8. 보험기간 (날짜를 선택해 주세요 : hint 문구) 클릭
            print("When: 8. 보험기간 (날짜를 선택해 주세요 : hint 문구) 클릭")
            el.click(Element.btn_period) # 보험기간 입력란 클릭
            time.sleep(2)
            # Then: 8. 출발일/도착일 선택 갤린더가 출력됨
            print("Then: 8. 출발일/도착일 선택 갤린더가 출력됨")
            result8 = el.is_visible(Element.text_period) # 바텀시트 출력 여부
            self.assertTrue(result8)
            print("Step8 Pass")

            # When: 9. 갤린더에 이틀 선택 후 [다음] 클릭
            print("When: 9. 갤린더에 이틀 선택 후 [다음] 클릭")
            # 현재 날짜를 기준으로 내일 날짜 계산
            today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            print(today)
            # 이틀 후 / 삼일 후 날짜를 타임스탬프로 변경
            twoday = today + datetime.timedelta(days=2)
            threeday = today + datetime.timedelta(days=3)
            # 이틀 후 / 삼일 후 날짜를 Unix 타임스탬프(ms 단위)로 변환
            twoday_timestamp = int(twoday.timestamp() * 1000)
            threeday_timestamp = int(threeday.timestamp() * 1000)
            print("이틀 후 타임스탬프:", twoday_timestamp)
            print("삼일 후 타임스탬프:", threeday_timestamp)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@data-time="{}"]'.format(twoday_timestamp)).click() # 이틀 후 클릭
            self.driver.find_element(By.XPATH, '//*[@data-time="{}"]'.format(threeday_timestamp)).click() # 삼일 후 클릭
            el.click(Element.btn_next) #[다음] 버튼 클릭
            # Then: 9. 선택한 날짜 저장되지 않고 갤린더 바텀시트 닫힘
            print("Then: 9. 선택한 날짜 저장되지 않고 갤린더 바텀시트 닫힘")
            result9 = el.is_visible(Element.text_period_edit) # 출발일 도착일 선택해주세요 문구
            self.assertTrue(result9)
            # 출발일 도착일 표시되는 형식으로 날짜 바꾸기
            formatted_twoday = twoday.strftime("%y.%m.%d")
            formatted_threeday = threeday.strftime("%y.%m.%d")
            print(formatted_twoday)
            print(formatted_threeday)
            # 출발일 정상 표시 여부 확인
            if str(formatted_twoday) in el.get_text(Element.text_start_day):
                result9_startday =  True
            else: result9_startday = False
            self.assertTrue(result9_startday)
            # 도착일 정상 표시 여부 확인
            if str(formatted_threeday) in el.get_text(Element.text_last_day):
                result9_lastday =  True
            else: result9_lastday = False
            self.assertTrue(result9_lastday)
            print("Step9 Pass")

            # When: 10. 가입하는 사람 (정보를 입력해 주세요 : hint 문구) 클릭
            print("When: 10. 선택한 날짜 저장되지 않고 갤린더 바텀시트 닫힘")
            el.click(Element.btn_user) # 가입하는 사람 입력란 클릭
            # Then: 10. 가입하는 사람의 정보를 입력해 주세요 바텀시트 출력됨
            print("Then: 10. 가입하는 사람의 정보를 입력해 주세요 바텀시트 출력됨")
            result10 = el.is_visible(Element.text_enter_subscriber) # 가입자 입력 영역 출력여부
            self.assertTrue(result10)
            print("Step10 Pass")

            """Step 11. 본인 인증 방법 관련 Skip or 자동화 테스트 가능한 방법 확인 필요"""

            """Step 12~16. Step 11이 선행되어야 동작 가능"""

        except NoSuchElementException:
            print("No Such Element Exception")
            self.assertTrue(False)
        except AssertionError:
            print("Assertion Error Occured")
            self.assertTrue(False)
        except:
            print("Unknown error")
            self.assertTrue(False)
