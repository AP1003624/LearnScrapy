# coding=utf-8
# author='吴俊'
# data=2015/8/27

# Redis是一个高性能的Kkey-value数据库。它将数据保存在内存中
# 安装scrapy-redis模块
# 安装和运行Redis
# 运行Redis：redis-server redis.conf
# 清空缓存：redis-cli flushdb


# Scrapy配置Redis
# # settings.py配置Redis
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# REDIS_URL = None
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379


# Spider调用Redis
# from scrapy_redis.spiders import RedisSpider
# class xxxx(RedisSpider):
#     ......