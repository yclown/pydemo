import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    headers = {'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Host':'maoyan.com',
               'Referer': 'http://maoyan.com/cinema/161?poi=123'
               }

    r=requests.get("http://maoyan.com/xseats/201811260140523?movieId=42964&cinemaId=16768",headers=headers)
    print(r.text)
    # text=open('ips.text','w',encoding='utf-8')
    # soup=BeautifulSoup(r.text, 'lxml')
    # for tr in soup('tr'):
    #     td=tr('td')
    #     if(len(td)>1):
    #         text.write('{0}|{1}|{2}\n'.format(td[5].get_text(),td[1].get_text(),td[2].get_text()))
    #         print(td[1].get_text())
    #     #print('ip {0} port:{1}'.format(td[1],td[2]))
    # text.close()