# coding=utf-8
# author='吴俊'
# data=2015/8/28


# Scrapy介绍与安装
# 安装lxml
# 安装zope.interface
# 安装Twisted
# 安装pyOpenSSL
# 安装pywin32
# 安装Scrapy（pip install scrapy）

# Scrapy爬取网页
# 核心代码：scrapy startproject xxx
# import scrapy
# from scrapy.contrib.spiders import CrawlSpider
# from scrapy.http import Request
# from scrapy.selector import Selector
# xxx = selector.xpath(xxxxx).extract()

# Scrapy文件结构
# project中的文件包括：
# items.py：定义需要抓取并需要后期处理的数据
# setting.py：配置Scrapy，从而修改user-agent，设定爬取时间间隔，设置代理，配置各种中间件等等
# pipelines.py：用于存放执行后期数据处理的能力，从而使得数据的爬取和处理分开












# 实战--豆瓣爬虫