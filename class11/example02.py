#selenium 사용
#pip install selenium
#pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager as cdm

import time

#크롬 드라이버 최신 버전 설정
service = Service(executable_path=cdm().install())
driver = webdriver.Chrome(service=service)

# 1. news를 가져온다.
# driver.get("https://www.naver.com/")
# print("네이버 들어감")
# time.sleep(2)
# ## 원하는 버튼을 누르는 명령을 한다. 뉴스 버튼 누름
# driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a").click()
# print("뉴스페이지 들어감")
# time.sleep(2)
# newstitle01 = driver.find_element(By.XPATH,"/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text
# print(newstitle01)
# newstitle02 = driver.find_element(By.XPATH,"/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[4]/a/div[2]/div").text
# print(newstitle02)
# time.sleep(10)

# 2. 아파트 가격 알아보기
# apt = "우성꿈동산"
# driver.get("https://m.land.naver.com/search")
# search = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input")
# search.click()
# time.sleep(1)
# search.send_keys(apt)
# time.sleep(1)
# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]").click()
# time.sleep(1)
# #전세값 가져오기
# rentPrice = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text
# print(apt)
# print("전세값 : ",rentPrice)

# 4. 주식 정보 가져오기
driver.get("https://finance.naver.com/")
# 거래 상위 3
top1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a").text
top2 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th/a").text
top3 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th/a").text
print(top1,top2,top3,sep=" | ")

lst = {
    '종목이름' : [],
    '주가' : []
       }
for i in range(1,10):
    subj = driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i}]/th/a").text
    lst["종목이름"].append(subj)
    price = driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i}]/td[1]").text
    lst["주가"].append(price)
    
stockDF = pd.DataFrame(lst)
print(stockDF)