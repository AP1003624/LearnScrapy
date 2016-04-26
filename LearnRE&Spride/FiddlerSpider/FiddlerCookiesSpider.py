# coding=utf-8
# author='吴俊'
# data=2015/8/26


# Cookies模拟登录——Fiddler获取Cookies
# 抓取登录数据包
# 获取Cookies
# Requests提交Cookies
# cookie = {"Cookies":"XXXXX"}
# Html = requests.get(url, cookies = cookie)
# 手机微博数据是html标签，更简洁，电脑版的数据是JSON样式

import requests
from lxml import etree


cook = {
    "Cookie":"_T_WM=f9abef1f849c62e5b260743c7d0d9d8d;SSOLoginState=1440920722;SUB=_2A2545sTBDeTxGedJ4lEW-CfPzjyIHXVYKOyJrDV6PUJbvNAKLVCtkW0dvPX3PVSTVMSJutLqC8doWUiFjQ..;SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5ysxrO0M9G_.cM0gaoYzCH5JpX5K-t;SUHB=0TPUHuR0spGzeO"
}
url = "http://weibo.cn/u/1890493665"
# print(cookie)
# 方法一：
html = requests.get(url, cookies=cook).content
# print(html)

# # 方法二：
# # html = requests.get(url, cookie).text
# # html = bytes(bytearray(html,"UTF-8"))
#
selector = etree.HTML(html)
content = selector.xpath('//span[@class="ctt"]')
for each in content:
    text = each.xpath("string(.)")
    b = 1
    print(text)