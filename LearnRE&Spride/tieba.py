# coding=utf-8
# author='吴俊'
# data=2015/8/24

import requests

# html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python')

html = requests.get('http://ext-mdskip.taobao.com/extension/dealRecords.htm?isOffline=&pageSize=15&isStart=false&itemType=b&ends=1453234176000&starts=1452629376000&itemId=44023105163&soldTotalNum=8944&sellerNumId=2112306610&isFromDetail=yes&totalSQ=124102&sbn=81380e9e4ceca9126e8e0731f74f529c&isSecKill=false&isOriginPrice=false&bidPage=1')
print(html.text)
