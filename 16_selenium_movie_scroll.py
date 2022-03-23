import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1980x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
           ,"Accept-Language":"ko-kr,ko"
           }
res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"hP61id"})
print(len(movies))

#with open("movies.html", "w", encoding="utf8") as f:
#    f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)



#페이지 이동
url = "https://www.google.com/search?q=%EC%98%81%ED%99%94&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjf1uv3-Nv2AhUFGqYKHVf8CbMQ_AUoAnoECAEQBA&biw=1280&bih=619&dpr=1.5"
browser.get(url)

#지정한 위치로 스크롤 내리기
#모니터(해상도) 높이인 1080 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,1080)") #1920 x 1080
#browser.execute_script("window.scrollTo(0,2080)") 

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이을 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #페이지 로딩 대기
    time.sleep(interval)
    
    # 현재 문서 높이을 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
    
print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")
browser.quit()