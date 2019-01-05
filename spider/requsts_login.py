import requests
from bs4 import BeautifulSoup

headers = {'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           }
def login(url):
    data = {
        'login':'1000',
        'pwd':'123456',
        'vendor':'',
        'token':'',
    }

    session = requests.session()
    content = session.post(url, data=data, headers=headers)
    return session
def getdata(sess,url,data):
    return sess.post(url,params=data, headers=headers)

if __name__ == '__main__':
    login_url="http://10.8.18.220/Login.aspx?login=true";
    data_url="http://10.8.18.220/hyedu/SchoolInfo/SchoolBusList.aspx?cmd=getdata"
    data={
        'SchoolName':'',
        'TwonID': '0',
        'SchoolTypeID': '0'

    }
    s =getdata(login(login_url),data_url,data)
    for school in s.json():

        print(school)