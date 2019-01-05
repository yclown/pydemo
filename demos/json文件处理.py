import os
import json
text=open("1.json",'r',encoding='utf-8')
myout=open('out.text','w',encoding='utf-8')
res= json.load(text)
for i in res:
    #print(i["txt"])
    myout.write(i["txt"])