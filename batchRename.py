import os

filelist=os.listdir('./LeetCode_rename')


print(filelist)
print(len(filelist))

# from urllib.request import urlopen 
# # 发出请求，获取html
# html = urlopen("https://leetcode.cn/problems/two-sum/")
# # 获取的html内容是字节，将其转化为字符串
# html_text = bytes.decode(html.read())
# # 打印html内容
# print(html_text)

# 导入urlopen函数
from urllib.request import urlopen
# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf
# 请求获取HTML
html = urlopen("https://leetcode.cn/problems/two-sum/")
# 用BeautifulSoup解析html
obj = bf(html.read(),'html.parser')
print(obj)
# 获取标签
tag=obj.select('#question-detail-main-tabs > div.css-1qqaagl-layer1.css-12hreja-TabContent.e16udao5 > div > div.css-xfm0cl-Container.eugt34i0 > h4 > a')
print(tag)
tag2=obj.find("h4",{"data-cypress": "QuestionTitle"}).get_text()
print(tag2)
# 从标签head、title里提取标题
title = obj.head.title
# 打印标题
print(title)

