# coding=utf-8
# author='吴俊'
# data=2015/8/24

# Get是从服务器上获取数据
# Post是向服务器传送数据
# Get通过构造url中的参数来实现功能
# POST是通过header提交数据

# Requests表单提交
# 核心方法：requests.post
# 核心步骤:构造表单—提交表单—获取返回信息
# 测试网站：https://www.crowdfunder.com/deals
# https://www.crowdfunder.com/deals&template=false

import requests
import re

# url1 = "https://www.crowdfunder.com/deals"
# html = requests.get(url1).text
# print(html)

url2 = "https://www.crowdfunder.com/deals&template=false"
formDate = {
    "entities_only":"true",
    "page":"2"
}
html_post = requests.post(url2, formDate).text
titles = re.findall('"card-title">(.*?)</div>', html_post, re.S)
for each in titles:
    print(each)