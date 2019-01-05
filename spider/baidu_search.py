import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               }
    req_url="https://www.baidu.com/s?ie=utf-8&wd=beautifulsoup4&pn=30"
    r = requests.get(req_url,headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    res=soup.find(id="content_left")
    for ba in res("div",class_="result"):
        #print(ba)
        print(ba.find("a").get_text())
        print(ba.find("a")["href"])
        '''print(ba["id"])'''
        print("------------------")
        #print(ba)
