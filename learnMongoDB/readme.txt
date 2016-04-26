MongoDB介绍与安装
    MongoDB的介绍：
        一个跨平台的NoSQL，基于Key-Value形式保存数据。起存储格式类似于Python的字典。
    MongoDB的安装：
        下载文件：https://www.mongodb.org/downloads
        创建文件夹：mkdir data
        执行命令：mongod --dbpath ./data(与mongod同目录下)
    MongoDB的可视化：MongoVUE




Python与MongoDB
    pymongo的安装：pip install pymongo
    Python操作MongoDB：
        import pymongo  导入第三方库
        connection = pymongo.MongoClient() 建立连接
        tdb = connection.Jikexueyuan  # 数据库名
        post_info = tdb.test  # 数据表名
        post_info.insert(xxxx)
        post_info.remove(xxxx)

Scrapy应用MongoDB
    配置文件的编写：
        在settings.py中配置MongoDB的IP地址、端口号、数据记录名称，可以实现方便的更换MongoDB的数据库信息
        在settings.py中引用pipelines.py从而使pipelines生效
    pipelines的编写：
        在pipelines中可以像普通Python文件操作MongoDB一样编写代码处理需要保存到MongoDB的数据。然而不同的是这里的数据来自items。这样做的好处是讲数据的抓取和处理分开。

实战--小说爬虫


