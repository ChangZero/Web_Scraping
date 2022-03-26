from attr import attrs
import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+%EB%A7%A4%EB%AC%BC&oquery=%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+%EC%8B%9C%EC%84%B8&tqi=hB8cswp0JXossRF%2BONdssssstCs-262166"
res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

# 분석하기 위해 html파일 만듬
# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

items = soup.find_all("tr", attrs={"class":"_land_tr_row"})
for index, item in enumerate(items):
    deal = item.find_all("td", attrs={"class":"fs_v2"})[0].get_text()
    name_source = item.find_all("td", attrs={"class":"fs_v2"})[1].get_text()
    cost = item.find("strong").get_text()
    area = item.find_all("td" , attrs={"class":"fs"})[0].get_text()
    
    print("===============매물 {}===============".format(index+1))
    print("거래 : " + deal)
    print("면적 : " + area)
    print("가격 : " + cost)
    print("출처 : " + name_source[-5:])
    print("동 :" + name_source[6:10])
