from wsgiref import headers
from attr import attrs
import requests
import re
from bs4 import BeautifulSoup


header = {"User-Agnet": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

for i in range(1,6):
    print("현재 페이지: ",i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)

    res = requests.get(url, headers= header)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())
    for item in items:
        #애플 제품 제외
        name = item.find("div", attrs={"class" : "name"}).get_text().strip()
        if "Apple" in name:
            continue
        
        price = item.find("strong", attrs = {"class":"price-value"}).get_text()
        rate = item.find("em", attrs = {"class":"rating"})
        rate_cnt = item.find("span", attrs = {"class":"rating-total-count"})
        link = item.find("a",attrs = {"class": "search-product-link"})["href"]

        if rate or rate_cnt:
            rate = rate.get_text()
            rate_cnt = rate_cnt.get_text()
        else:
            continue
            
        #평점 4.5이상 리뷰수 300개 이상
        if float(rate)>=4.5 and int(rate_cnt[1:-1])>=300:
            print(f"제품명: {name}")
            print(f"가격: {price}")
            print(f"평점: {rate}점 {rate_cnt}개")
            print("바로가기: {}".format("https://www.coupang.com" + link))
            print("-"*100)
            