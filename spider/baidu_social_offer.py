import requests
from urllib import parse
import json
from bs4 import BeautifulSoup
if __name__ == '__main__':
    headers = {'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               }
    data={
        'postType':'',
        'workPlace': '0/4/7/9',
        'recruitType': '2',
        'keyWord':'',
        'pageSize': '100',
        'curPage': '1',

    }
    #params = parse.urlencode(data).replace('+','%20')
    #print(params)
    req_url="https://talent.baidu.com/baidu/web/httpservice/getPostList"
    #print(req_url)
    r = requests.get(req_url, headers=headers,params=data)

    res=r.json()
    #print(res["postList"])
    #soup = BeautifulSoup(r.text, 'lxml')
    #soup.p.get_text()
    #res = json.load()
    i=0
    for offer in res["postList"]:
        i += 1
        print('{0}   {1}'.format(i, offer["name"]))


