# coding=utf-8
# author='吴俊'
# data=2015/8/26

# 目标网站：http://tieba.baidu.com/p/3522395718
# 目标内容：跟帖用户名，跟帖内容，更贴时间
# 涉及内容：Requests获取网页、XPath提取内容、map实现多线程爬虫

from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
headers = {'User_Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27'}

def towrite(contentdic):
    tieba.writelines("回帖时间："+str(contentdic['topic_reply_time'])+'\n')
    tieba.writelines("回帖内容："+unicode(contentdic['topic_reply_content'])+'\n')
    tieba.writelines("回帖人："+contentdic['user_name']+'\n\n')


def spider(url):
    # html = requests.get(url)
    # selector = etree.HTML(html.text)
    # content_field = selector.xpath('//div[@class="l_post l_post_bright  "]')
    # item = {}
    # for each in content_field:
    #     reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',''))
    #     author = reply_info['author']['user_name']
    #     content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')[0]
    #     print(content)
    #     reply_time = reply_info['content']['date']
    #     print content
    #     print reply_time
    #     print author
    #     item['user_name'] = author
    #     item['topic_reply_content'] = content
    #     item['topic_reply_time'] = reply_time
    #     towrite(item)
    html = requests.get(url, headers)
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//div[@class="l_post l_post_bright  "]')
    item = {}
    for each in content_field:
        print(each)
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',''))
        author = reply_info['author']['user_name']
        content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')[0]
        print(content)
        reply_time = reply_info['content']['date']
        print(content)
        print(reply_time)
        print(author)
        item['user_name'] = author
        item['topic_reply_content'] = content.replace(' ', '')
        item['topic_reply_time'] = reply_time
        towrite(item)

if __name__ == '__main__':
    pool = ThreadPool(4)
    tieba = open('content.txt', 'a')
    # page = ['http://tieba.baidu.com/p/3522395718?pn=2']
    page = []
    for i in range(1, 21):
        newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
        page.append(newpage)
    print(page)
    results = pool.map(spider, page)
    pool.close()
    pool.join()
    tieba.close()