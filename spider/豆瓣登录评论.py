import requests
import os
import time
from bs4 import BeautifulSoup
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
    proxies = {
        "http":"http://222.190.126.62:808 ",
    }
