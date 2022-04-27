import urllib
from urllib.request import urlopen

from selenium import webdriver
import getpass

from time import sleep

import pandas as pd

# 크롬 드라이버 열기
driver = webdriver.Chrome("./chromedriver")  # Chromedriver PATH
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window() # 창 최대화하기

username = getpass.getpass("인스타그램 계정을 입력해주세요 : ")  # ID
password = getpass.getpass("인스타그램 비밀번호를 입력해주세요 : ")  # Password

element_id = driver.find_element_by_name("username") # input 태그의 name 옵션이 username인 element를 찾아줘
element_id.send_keys(username) # 키보드의 키를 PC에 전달할 수 있음
element_password = driver.find_element_by_name("password")
element_password.send_keys(password)

sleep(1.5)

# 로그인 버튼
driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF').click()

sleep(4)

# 로그인 정보 저장 나중에 하기
driver.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF').click()

# 알림 설정 나중에 하기
driver.find_element_by_css_selector('button.aOOlW.HoLwm').click()

# 인스타그램 개인 계정 https://www.instagram.com/{username}/
# driver.get("https://www.instagram.com/myunbongs/")

# pandas로 엑셀 파일 가져오기
df = pd.read_excel('likelion_smu_insta.xlsx')

#print(df)

# print(df["insta_id"])

df = df["insta_id"].dropna(axis=0)

#print(df)

def scroll():
    # 스크롤을 내려서 모든 게시물 얻기
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    timer = 1
    while (timer<5):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        sleep(SCROLL_PAUSE_TIME)
        timer=timer+1

baseURL = "https://www.instagram.com/"


for username in df:
    count = 0
    driver.get(baseURL + username + "/")
    scroll()
    images = driver.find_elements_by_css_selector("img.FFVAD")

    # print(username + "님의 글 개수:" + len(images))

    for image in images:
        try:
            sleep(2)
            imgUrl = image.get_attribute("src")
            urllib.request.urlretrieve(imgUrl, "./results/" + username  + "_" + str(count) + ".jpg")
            sleep(1)
            count = count + 1
        except:
            pass

    print(username + "님의 인스타그램 염탐 완료!")




