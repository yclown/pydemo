import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    headers = {
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Win64; x64; Trident/7.0)',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               }
    proxies = {"http": "http://222.190.126.62:808"}
    r=requests.get("http://maoyan.com/xseats/201811260140523?movieId=42964&cinemaId=16768",headers=headers)
    html = r.content
    html_doc = str(html, 'utf-8')  # html_doc=html.decode("utf-8","ignore")
    print(html_doc)
    soup=BeautifulSoup(html_doc, 'lxml')
    res=soup.find(class_='getlist')
    print(res)
