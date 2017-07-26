#셀레니움 크롬드라이버 쓸 때 이미지 안 뜨게 하는 코드
#기존 driver = webdriver.Chrome() 자리에 아래의 코드를 대신 적으면 됩니다.


chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
