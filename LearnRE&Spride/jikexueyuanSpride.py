# coding=utf-8
# author='吴俊'
# data=2015/8/24

# 目标网站：http://www.jikexueyuan.com/course/
# 目标内容：课程名称，课程介绍，课程时间，课程等级，学习人数
# 涉及知识：Requests获取网页、re.sub换页、正则表达式匹配内容

# http://www.jikexueyuan.com/course/?pageNum=1

import requests
import re

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'}
url = 'http://www.jikexueyuan.com/course/'
html = requests.get(url, header).text
html.encode('utf-8')
# print(html)
# 先按课程模块匹配
contxts = re.findall('<div class="lesson-infor"(.*?)<div class="lessonicon-box">', html, re.S)
#按具体内容匹配
for each in contxts:
    # print(each)
    # print("===============")
    # 匹配课程名称
    courseName = re.search('jktag="(.*?)">(.*?)</a></h2>', each, re.S).group(2)
    print(courseName)
    # 匹配课程介绍
    courseDes = re.search('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>', each, re.S).group(1)
    print(courseDes)
    # 匹配课程时间
    courseTime = re.search('<i class="time-(.*?)"></i><em>(.*?)</em>', each, re.S).group(2)
    print(courseTime)
    # 匹配课程等级
    courseLev = re.search('<i class="xinhao-(.*?)"></i><em>(.*?)</em>', each, re.S).group(2)
    print(courseLev)
    # 匹配学习人数
    courseNum = re.search('<em class="learn-(.*?)">(.*?)</em>', each, re.S).group(2)
    print(courseNum)
