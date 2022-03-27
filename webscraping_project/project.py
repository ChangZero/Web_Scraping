import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://weather.naver.com/"
    soup = create_soup(url)
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    current_tmp = soup.find("strong", attrs={"class":"current"}).get_text()
    low_tmp = soup.find("span", attrs={"class":"data lowest"}).get_text()
    high_tmp = soup.find("span", attrs={"class":"data highest"}).get_text()

    print(cast.replace(" ", ""))
    print(current_tmp)
    print("최적기온: " + low_tmp[4:])
    print("최고기온: "+ high_tmp[4:])
    
    
def scarpe_headline_news():
    print("[헤드라인뉴스]")
    url = "https://news.daum.net/"
    soup = create_soup(url)
    news_list = soup.find("div", attrs={"class":"content-article"}).find_all("a",attrs = {"class":"link_txt"})
    for index, news in enumerate(news_list):
        if index > 4:
            break       
        print(str(index+1) + "번 " + news.get_text().replace("\n"," ").strip())
        link = news["href"]
        print("(링크: {})".format(link))

if __name__ == "__main__":
    scrape_weather()
    scarpe_headline_news()
    
    