import requests
from bs4 import BeautifulSoup
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#attributes
#操作手册
if __name__ == '__main__':
    r=requests.post("https://blog.csdn.net/column/details/15321.html")
    soup=BeautifulSoup(r.text, 'lxml')
    #t_list = soup(class_="blog_l")
    # print(t_list[0]["class"])  #['blog_l', 'fl']

    t_list = soup.find(class_="detail_list")
    #print(t_list("li"))
    for li in t_list("li"):
        print(li.a.string)
        print(li.a["href"])