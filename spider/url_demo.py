from urllib import request,parse
import chardet
#基础演示
url = 'http://fanyi.baidu.com/'

response = request.urlopen(url)
html = response.read()
#获取网页编码
charset = chardet.detect(html)
# print(html.decode(charset['encoding']))
print(response.info())