# coding=utf-8
# author='吴俊'
# data=2015/8/25

# XPath通过元素和属性进行导航，比正则表达式更厉害和简单
# 属于lxml库
# from lxml import etree
# Selector = etree.HTML(网页源码）
# Selector.xpath(一段神奇的符号)
# 获取XPath：使用Chrome浏览器开发工具，选中相应节点右击选择“Copy XPath”
# 应用XPath提取内容：
# //定位根节点
# /往下层寻找
# 提取文本内容：/text()
# 提取属性内容：/@xxxx

from lxml import etree

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试-常规用法</title>
</head>
<body>
<div id="content">
    <ul id="useful">
        <li>这是第一条信息</li>
        <li>这是第二条信息</li>
        <li>这是第三条信息</li>
    </ul>
    <ul id="useless">
        <li>不需要的信息1</li>
        <li>不需要的信息2</li>
        <li>不需要的信息3</li>
    </ul>
    <div id="url">
        <a href="http://jikexueyuan.com" title="极客学院">极客学院</a>
        <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
    </div>
</div>

</body>
</html>
'''

selector = etree.HTML(html)

# 提取文本
content = selector.xpath('//ul[@id="useful"]/li/text()')
for each in content:
    print(each)

# 提取属性
links = selector.xpath('//a/@href')
for each in links:
    print(each)

# 提取标题
titles = selector.xpath('//a/@title')
for each in titles:
    print(each)

print(titles[0])

