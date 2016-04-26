# coding=utf-8
# author='吴俊'
# data=2015/8/24

# 测试链接：http://www.jikexueyuan.com/course/android/?pageNum=2
import re
old_url = "http://www.jikexueyuan.com/course/android/?pageNum=2"
total_page = 20
f = open('text.txt', 'r')
html = f.read()
f.close()
print(html)

# 爬虫标题
title = re.search("<title>(.*?)</title>", html, re.S).group(1)
print(title)

# 爬虫链接
links = re.findall('href="(.*?)"', html, re.S)
for each in links:
    print(each)

# 爬取部分文字，先大再小
text_fied = re.findall('<ul>(.*?)</ul>', html, re.S)[0]
the_text = re.findall('">(.*?)</a>', text_fied, re.S)
for every_text in the_text:
    print(every_text)

# sub实现翻页
for i in range(2, total_page+1):
    new_linke = re.sub('pageNum=\d+', 'pageNum=%d' %i, old_url)
    print(new_linke)
