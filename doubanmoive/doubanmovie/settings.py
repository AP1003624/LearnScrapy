# -*- coding: utf-8 -*-

# Scrapy settings for doubanmovie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanmovie'

SPIDER_MODULES = ['doubanmovie.spiders']
NEWSPIDER_MODULE = 'doubanmovie.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanmovie (+http://www.yourdomain.com)'

FEED_URI = "file:///D:/Python/PythonWorkSpace/LearnScrapy/doubanmoive/douban.csv"
FEED_FORMAT = 'CSV'


