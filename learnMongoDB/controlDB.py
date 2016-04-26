# coding=utf-8
# author='吴俊'
# data=2015/8/31

import pymongo
# import sys
# reload(sys)
# sys.setdefaultencoding('gbk')

connection = pymongo.MongoClient()
tdb = connection.Jikexueyuan  # Jikexueyuan是数据库名
post_info = tdb.test  # test是表名
like = {'name':u'极客学院1', 'age': '5', 'skill':'Python'}
god = {'name': u'玉皇大帝1', 'age':3600, 'skill':'creatanything','other':u'王母娘娘不是他老老婆'}
godslaver = {'name':u'月老1','age':'unknown','other':u'他老婆叫孟婆'}
post_info.insert(like)
post_info.insert(god)
post_info.insert(godslaver)  # 添加数据
post_info.remove({'name': u'极客'})  # 删除数据
print(u'操作数据库完成！')
for each in post_info.find():
    print(each)
