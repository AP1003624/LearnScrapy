# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class LearnmongodbItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NovelspiderItem(Item):
    bookName = Field()
    bookTitle = Field()
    chapterNum = Field()
    chapterName = Field()
