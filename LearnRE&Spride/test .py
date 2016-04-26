# coding=utf-8
# author='吴俊'
# data=2015/8/24

import requests
import re

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'}
url = 'http://www.jikexueyuan.com/course/'
html = requests.get(url, header).text

# 先按课程模块匹配
contxts = re.findall('<div class="lesson-infor"(.*?)<div class="lessonicon-box">', html, re.S)

#按具体内容匹配
for text in contxts:
    # print(text)
    # 匹配课程名称
    courseName = re.search('jktag="(.*?)">(.*?)</a></h2>', text, re.S).group(2)
    print(courseName)
    # # 匹配课程介绍
    courseDes = re.search('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>', text, re.S).group(1)
    print(courseDes.strip())
    # # 匹配课程时间
    courseTime = re.search('<i class="time-(.*?)"></i><em>(.*?)</em>', text, re.S).group(2)
    print(courseTime.strip())
    # # 匹配课程等级
    courseLev = re.search('<i class="xinhao-(.*?)"></i><em>(.*?)</em>', text, re.S).group(2)
    print(courseLev.strip())
    # 匹配学习人数
    courseNum = re.search('<em class="learn-(.*?)">(.*?)</em>', text, re.S).group(2)
    print(courseNum.strip())



