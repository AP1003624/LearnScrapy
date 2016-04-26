# coding=utf-8
# author='吴俊'
# data=2015/8/24

import re
import requests

# 读取源代码文件
f = open('source.txt', 'r')
html = f.read()
f.close()

# 匹配图片网址
pic_url = re.findall('img src="(.*?)" class="lessonimg"', html, re.S)
i = 0
for each in pic_url:
    print('now download:')+each
    pic = requests.get(each)
    fp = open('pic\\'+str(i)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1