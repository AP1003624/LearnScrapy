MongoDB�����밲װ
    MongoDB�Ľ��ܣ�
        һ����ƽ̨��NoSQL������Key-Value��ʽ�������ݡ���洢��ʽ������Python���ֵ䡣
    MongoDB�İ�װ��
        �����ļ���https://www.mongodb.org/downloads
        �����ļ��У�mkdir data
        ִ�����mongod --dbpath ./data(��mongodͬĿ¼��)
    MongoDB�Ŀ��ӻ���MongoVUE




Python��MongoDB
    pymongo�İ�װ��pip install pymongo
    Python����MongoDB��
        import pymongo  �����������
        connection = pymongo.MongoClient() ��������
        tdb = connection.Jikexueyuan  # ���ݿ���
        post_info = tdb.test  # ���ݱ���
        post_info.insert(xxxx)
        post_info.remove(xxxx)

ScrapyӦ��MongoDB
    �����ļ��ı�д��
        ��settings.py������MongoDB��IP��ַ���˿ںš����ݼ�¼���ƣ�����ʵ�ַ���ĸ���MongoDB�����ݿ���Ϣ
        ��settings.py������pipelines.py�Ӷ�ʹpipelines��Ч
    pipelines�ı�д��
        ��pipelines�п�������ͨPython�ļ�����MongoDBһ����д���봦����Ҫ���浽MongoDB�����ݡ�Ȼ����ͬ�����������������items���������ĺô��ǽ����ݵ�ץȡ�ʹ���ֿ���

ʵս--С˵����


