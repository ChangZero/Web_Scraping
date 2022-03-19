from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename = "사가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig",newline="") #보통은 utf8 을 사용하지만 엑셀에서 열때 한글이 깨질수 있음 따라서 위와같이 바꿔서 사용!
writer = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs = {"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td") 
        if len(columns) <= 1: #의미없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data)