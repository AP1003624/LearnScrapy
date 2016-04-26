# coding=utf-8
# author='吴俊'
# data=2015/8/26

# 模拟新浪微博登录
# 分析需要提交的数据
# Mobile：用户名
# Password：密码
# remember：是否保存登录
# backURL：登录以后返回的地址
# backTitle：登录以后返回的标题
# tryCount：尝试次数
# vk：一个简单的验证码
# submit：登录
# action：URL参数

# Requests提交数据
# data = {
#     "mobile":"xxxxx",
#     "password":"xxxx",
#     .....
# }
#
# Html = requests.post(url, data)

import requests
from lxml import etree
url = "http://weibo.cn/u/1890493665"
url_login = "http://login.weibo.cn/login/"
html = requests.get(url).content
selector = etree.HTML(html)
password = selector.xpath('//input[@type="password"]/@name')[0]
vk = selector.xpath('//input[@name="vk"]/@value')[0]
action = selector.xpath('//form[@method="post"]/@action')[0]
print(action)
print(password)
print(vk)

new_url = url_login + action
data = {
    'mobile': '646706230@qq.com',
    password: 'ZXCASDQWE129526',
    'remember': 'on',
    # 'backURL': 'http%3A%2F%2Fweibo.cn%2Fu%2F1890493665',
    'backTitle': u'微博',
    'tryCount': '',
    'vk': vk,
    'submit':  u'登录'
}


newhtml = requests.post(new_url, data).content
new_selector = etree.HTML(newhtml)
print(newhtml)
