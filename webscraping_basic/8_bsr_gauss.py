import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


# 만화제목과 링크 가져오기
# cartoons = soup.find_all("td", attrs={"class":"title"})
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

total_rates = 0
cartoons = soup.find_all("div", attrs = {"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수: ", round(total_rates,2))
print("평균 점수: ", round(total_rates/len(cartoons),2))