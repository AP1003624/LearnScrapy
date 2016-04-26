# coding=utf-8
# author='吴俊'
# data=2015/8/27

# 追女神助手V0.1(定向爬虫)
# 目标网站：新浪微博
# 目标内容：微博内容
# 功能太简单，可扩充功能：
# 爬取关注列表，从而分析社交关系网络
# 爬取全部微博内容，分析性格与喜好（词频）
# 爬不是目的，爬是为了实现目的

import smtplib
from email.mime.text import MIMEText  # Python邮件库
import requests
from lxml import etree
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class mailhelper(object):  # 这个类日后可以直接使用
    '''
    这个类实现发送邮件功能
    '''
    def __init__(self):
        self.mail_host = "smtp.qq.com"  # 设置服务器
        self.mail_user = "646706230"  # 用户名
        self.mail_pass = "ZXCASDQWE129526"  # 口令
        self.mail_postfix = "qq.com"  # 发件箱的后缀

    def send_mail(self, to_list, sub, content):
        me = "xxoohelper"+"<"+self.mail_user+"@"+self.mail_postfix+">"
        msg = MIMEText(content, 'plain', 'UTF-8')  # 将内容转化成邮件可识别格式
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print(str(e))
            return False

class xxoohelper(object):
    '''
    这个类实现将爬取微博第一条内容
    '''
    def __init__(self):
        self.url = 'http://weibo.cn/u/1890493665'
        self.url_login =  "http://login.weibo.cn/login/"
        self.new_url = self.url_login

    def getSource(self):
        html = requests.get(self.url).content
        return html

    def getData(self, html):
        selector = etree.HTML(html)
        password = selector.xpath('//input[@type="password"]/@name')[0]
        vk = selector.xpath('//input[@name="vk"]/@value')[0]
        action = selector.xpath('//form[@method="post"]/@action')[0]
        self.new_url = self.url_login + action
        data = {
            'mobile': '646706230@qq.com',
            password: 'ZXCASDQWE129526',
            'remember': 'on',
            # 'backURL': 'http%3A%2F%2Fweibo.cn%2Fu%2F1890493665', # action已经带了
            'backTitle': u'微博',
            'tryCount': '',
            'vk': vk,
            'submit':  u'登录'
        }
        return data

    def getContent(self, date):
        newhtml = requests.post(self.new_url, data).content
        # print(newhtml)
        new_selector = etree.HTML(newhtml)
        content = new_selector.xpath('//span[@class="ctt"]')
        newcontent = unicode(content[2].xpath('string(.)')).replace('http://', '')
        sendtime = new_selector.xpath('//span[@class="ct"]/text()')[0]
        sendtext = newcontent + sendtime
        return sendtext

    def tosave(self, text):
        f = open('weibo.txt', 'a')
        f.write(text + '\n')
        f.close()

    def tocheck(self, data):
        if not os.path.exists('weibo.txt'):
            return True
        else:
            f = open('weibo.txt', 'r')
            existweibo = f.readline()
            if data + '\n' in existweibo:
                return False
            else:
                return True

if __name__ == '__main__':
        mailto_list = ['646706230@qq.com']
        helper = xxoohelper()
        while True:
            source = helper.getSource()
            data = helper.getData(source)
            content = helper.getContent(data)
            if helper.tocheck(content):
                if mailhelper().send_mail(mailto_list, '女神更新啦', content):
                    print("发送成功")
                else:
                    print("发送失败")
                helper.tosave(content)
                print(content)
            else:
                print("pass")
            time.sleep(30)  # 微博扫描时间差


