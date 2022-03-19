from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com"
browser.get(url)

browser.find_elements(By.CLASS_NAME,"select_name__1L61v")[1].click() #도착 선택 누르기
time.sleep(1)
browser.find_elements(By.CLASS_NAME,"autocomplete_Collapse__tP3pM")[1].click() #국가 선택
browser.find_elements(By.CLASS_NAME,"autocomplete_Airport__3_dRP")[0].click() #도시(공항)선택


browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click() #가는 날 선택하기
time.sleep(1)
#가는 날짜 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[3]/button/b").click()
time.sleep(1)
#오는 날짜 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[5]/button").click()
time.sleep(1)
#검색 버튼 누르기
browser.find_element(By.CLASS_NAME,"searchBox_search__2KFn3").click()

#로딩시 설정시간동안 값을 받아오면 try문 실행!
try:
    infos = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"routes")))
    costs = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"item_price__1TxJh")))
    for info, cost in zip(infos,costs):
        print("비행정보:") 
        print(info.text)
        print("가격: ",cost.text)
finally:
    browser.quit()
    
