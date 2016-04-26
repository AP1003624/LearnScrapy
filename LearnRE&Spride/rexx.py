# coding=utf-8
# author='吴俊'
# data=2015/8/24

# 导入re包
import re

secret_code = 'hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'


# .的使用
a = "xy123"
print(re.findall("x", a))
print(re.findall("x.", a))
print(re.findall("x..", a))
print(re.findall("x...", a))

# *的使用
a = "xyxy123"
print(re.findall("x*", a))

# ?的使用
print(re.findall("x?", a))

# 贪心算法(.*)的使用
print(re.findall("xx.*xx", secret_code))

# 非贪心算法(.?*)的使用
print(re.findall("xx.*?xx", secret_code))
print(re.findall("xx(.*?)xx", secret_code))  # 重点掌握这一种即可


s = '''sdfxxhello
xxfsdxxworldxxasdf'''
print(re.findall("xx(.*?)xx", s))
print(re.findall("xx(.*?)xx", s, re.S))  # re.S用来比配比配任意一行，包括换行符。而.匹配不包括换行符

# 对比findall和search的区别
s2 = 'asdfxxIxx123xxlovexxafd'
f = re.search("xx(.*?)xx123xx(.*?)xx", s2).group(2) # gropu用来匹配第N个(.*?)的内容
print(f)
f2 = re.findall("xx(.*?)xx123xx(.*?)xx", s2)
print(f2[0][1])

# sub的使用
s3 = "123abcssfasdfas123"
output = re.sub("123(.*?)123", "123%d123" %789, s3)
print(output)

# 匹配纯数字
a = "asdfasf1234567fasd555fas"
print(re.findall("(\d+)", a))
