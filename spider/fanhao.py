from urllib import request
from bs4 import BeautifulSoup
if __name__ == '__main__':

    proxies = {"http": "http://222.190.126.62:808"}
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D)' \
                         ' AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    for i in range(3,50):
        url = "http://www.17fanhao.com/fanhao/index_{0}.html".format(i)
        req = request.Request(url, headers=head)
        response = request.urlopen(req)
        soup=BeautifulSoup( response.read())
        content=soup.find(class_='movie_list')
        for info in content('li'):
            try:
                f = open('Temp\\' + info.find('img')['alt'] + ".jpg", 'wb')
                f.write((request.urlopen(info.find('img')['src'])).read())
                #print(imgPath)
                f.close()
            except Exception as e:
                print(e)
            print(info.find('img')['src'])
            print(info.find('img')['alt'])
