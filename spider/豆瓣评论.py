import requests
import os
import time
from bs4 import BeautifulSoup
import random
def getip():
    ips = open('ips.text', 'r')
    res=[]
    for ip in ips.readlines():
        item=ip.replace('\n','').split('|')
        res.append(item[1]+':'+item[2])
    return res
if __name__ == '__main__':
    headers = {'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               }
    data={
        'start':0,
        'limit':'20',
        'sort':'new_score',
        'status':'P'

    }


    text=open("一出好戏.txt",'w',encoding="utf-8")
    req_url="https://movie.douban.com/subject/26985127/comments"
    count=0
    ips=getip()
    for i in range(100):
        #time.sleep(1)
        data["start"]=i*20
        r = requests.get(req_url, headers=headers, proxies={'http':random.choice(ips)},params=data)

        soup = BeautifulSoup(r.text, 'lxml')
        for comm in soup(class_='short'):
            count+=1
            print(count)
            print(comm.get_text())
            text.write(comm.get_text()+"\n\n")
            print("-------------")



    text.close()