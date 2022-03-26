import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1980x1080")
#headless 사용할때 user-agent값으 주고 싶다면 사용(왜 사용하냐면 headless를 사용하면 접근을 막는 웹사이트들이 있음 간혹..)
options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/99.0.4844.82 Safari/537.36
detected_value =  browser.find_element(By.ID, "detected_value")
print(detected_value.text)
browser.quit()