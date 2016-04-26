# coding=utf-8
# author='吴俊'
# data=2015/8/28

import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from doubanmovie.items import DoubanmovieItem

class Douban(CrawlSpider):
    name = 'doubanmovie'
    redis_key = 'douban:strat_urls'
    start_urls = ['http://movie.douban.com/top250']

    url = 'http://movie.douban.com/top250'  # 合成翻页链接

    def parse(self, response):
        # print(response.body)
        item = DoubanmovieItem()
        selector = Selector(response)
        movies = selector.xpath('//div[@class="info"]')
        for eachMovie in movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span/em/text()').extract()[0]
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # quote可能为空，因此需要先进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)  # 用分号进行分割
            item['star'] = star
            item['quote'] = quote
            yield item  # 将item提交到csv文件中
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            print(nextLink)
            yield Request(self.url + nextLink, callback=self.parse)