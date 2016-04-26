# coding=utf-8
# author='吴俊'
# data=2015/8/24

import requests
import re
import sys

reload(sys)
sys.setdefaultencoding("gb18030")
type = sys.getfilesystemencoding()

# 修改http中header
headers = {'User_Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27'}
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/', headers)
html.encoding = 'utf-8'
print(html.text)
titles = re.findall('color: #039;">(.*?)</a>', html.text, re.S)
for each in titles:
    print(each)

# 日本变成中文


