# coding=utf-8
# author='吴俊'
# data=2015/8/28

from scrapy.spiders import CrawlSpider
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Douban(CrawlSpider):
    name = "doubanTest" # 爬虫名
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        print(response.body)
        print(response.url)
