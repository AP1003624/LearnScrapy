# -*- coding: utf-8 -*-

# Scrapy settings for learnRedis project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'learnRedis'

SPIDER_MODULES = ['learnRedis.spiders']
NEWSPIDER_MODULE = 'learnRedis.spiders'


SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
REDIS_URL = None
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379