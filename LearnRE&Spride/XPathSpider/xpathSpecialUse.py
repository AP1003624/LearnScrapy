# coding=utf-8
# author='吴俊'
# data=2015/8/26
# XPath的特殊用法

from lxml import etree
# 以相同的字符开头
# starts-with(@属性名称，属性字符相同部分)
html1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<div id="test-1">需要的内容1</div>
<div id="test-2">需要的内容2</div>
<div id="testfault">需要的内容3</div>
</body>
</html>
'''
selector = etree.HTML(html1)
contents = selector.xpath('//div[starts-with(@id,"test")]/text()')
for each in contents:
    print(each)


# 标签套标签
# string(.)
html2 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<div id="test3">
    我左青龙，
    <span id="tiger">
        右白虎，
            <ul>
                上朱雀，
                <li>下玄武。</li>
            </ul>
    </span>
    龙头在胸口。
</div>
</body>
</html>
'''
selector = etree.HTML(html2)
contents = selector.xpath('//div[@id="test3"]/text()')
for each in contents:
    print(each)

contents = selector.xpath('//div[@id="test3"]')[0]
info = contents.xpath('string(.)')
data = info.replace('\n', '').replace(' ', '')
print(data)