import os
import matplotlib.pyplot as plt
from scipy.misc import imread
from collections import Counter
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba
import jieba.analyse

import sys
jieba.load_userdict("dict.txt")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

stopwords_path='stop.txt'

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path,'r',encoding="utf-8")
    try:
        f_stop_text = f_stop.read( )
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

text=open("../demos/out.text",'r',encoding='utf-8')
words=text.read()

def wordcloudshow(words):
    cut_text=jiebaclearText(words)
    color_mask = imread("1.png")
    cloud = WordCloud(
        background_color='white',#设置背景颜色
        mask=color_mask,#背景图片
        font_path='simkai.ttf',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        max_words=2000,#设置最大显示的字数
        stopwords=STOPWORDS,#设置停用词
        max_font_size=150,#设置字体最大值
        random_state=30 #设置有多少种随机形态，即多少种配色方案
    )
    word_cloud = cloud.generate(cut_text)
    plt.imshow(word_cloud)#显示词云图
    plt.axis('off')#不显示x、y轴
    plt.show()
def bar(words):
    keywords = jieba.analyse.extract_tags(words, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    labels = []
    fracs = []
    for i in keywords:
        labels.append(i[0])
        fracs.append(i[1] * 100)
    plt.bar(left=labels, height=fracs, color='green', width=0.8)   #条形图
    plt.show()
bar(words)
#wordcloudshow(words)