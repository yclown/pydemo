# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar
from bs4 import BeautifulSoup
# https://blog.csdn.net/c406495762/article/details/71158264
if __name__ == '__main__':
    #登陆地址
    login_url = 'http://10.8.18.220/Login.aspx?login=true'
    #User-Agent信息
    user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    #Headers信息
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    #登陆Form_Data信息
    Login_Data = {}
    Login_Data['login'] = '1000'
    Login_Data['pwd'] = '123456'
    Login_Data['vendor'] = ''         #是否一个月内自动登陆
    Login_Data['token'] = ''       #改成你自己的用户名

    #使用urlencode方法转换标准格式
    logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
    #声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(cookie_support)
    #创建Request对象
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head)

    #面向对象地址
    date_url = 'http://10.8.18.220/hyedu/Search/SchoolSearch.aspx'

    req2 = request.Request(url=date_url, headers=head)
    try:
        #使用自己创建的opener的open方法
        response1 = opener.open(req1)
        response2 = opener.open(req2)
        html = response2.read().decode('utf-8')
        #index = response1.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')

        print(soup.body.contents[1])

    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError:%d" % e.code)
        elif hasattr(e, 'reason'):
            print("URLError:%s" % e.reason)