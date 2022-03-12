# bs4는 한글문서가 제공된다 더 자세하게 알기위헤서는 구글에 beautifulsoup검색후 document찾기

import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.title)   #
# print(soup.title.get_text())
# print(soup.a)   #soup객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element의 속성 정보
# print(soup.a["href"])   # a element 의 href의 속성 정보 가져옴

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class값으로 a element를 찾아줘

rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent)

# rank2= rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank2 = rank2.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="전지적 독자 시점-093. Ep. 20 범람의 재앙 (1)")
print(webtoon)