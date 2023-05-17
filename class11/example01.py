#0517
#beautifulsoup4 사용
#pip install beautifulsoup4
from bs4 import BeautifulSoup as Bsoup
import requests as rq # http 관련 해결해 주는 모듈

'''
url을 입력 받으면 DNS(Domain Name Server)로 Requests보냄
구글 DNS 서버 8.8.8.8
그에 대한 Response로 해당 서버의 ip주소를 보내줌
'''

headers = {
    "User-Agent" : "JaeSeok"
}
# 우크라이나 뉴스 스크랩
webPage = rq.get("https://n.news.naver.com/mnews/article/658/0000041216?sid=104", headers=headers)
#print(webPage)
#print(webPage.content)
soupedPage = Bsoup(webPage.content, "html.parser")
#print(soupedPage)
ukrContent = soupedPage.select_one("#dic_area").get_text().strip()
#print(ukrContent)

# 마케팅 뉴스 스크랩
soupedNews = Bsoup(rq.get("https://n.news.naver.com/mnews/article/015/0004845610?sid=105", headers=headers).content,"html.parser")
newsTitle = soupedNews.select_one("#title_area").get_text()
newsContent = soupedNews.select_one("#dic_area").get_text().strip()
print(newsTitle,'\n')
print(newsContent)