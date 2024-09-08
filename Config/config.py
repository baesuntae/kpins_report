
url_info = {
    "interpark" : "https://talk.kakaoinsure.com/partner/plan/FAA004?campaignCode=TRP2312001&dc=TRP301",
    "hyundai" : "https://talk.kakaoinsure.com/partner/plan/FAA004?campaignCode=HDC2403001&dc=HDC200"
     }


class EnvVar:
    __instance = None
    test_url = "interpark"


    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = EnvVar()
        return cls.__instance