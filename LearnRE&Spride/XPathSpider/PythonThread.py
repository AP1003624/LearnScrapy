# coding=utf-8
# author='吴俊'
# data=2015/8/26
# Python并行化介绍与演示

# map的使用
# from multiprocessing.dummy import  Pool
# pool = Pool(电脑核数)
# results = pool.map(爬取函数，网址列表)
# pool.close()
# pool.join()

from multiprocessing.dummy import Pool as  ThreadPool
import requests
import time

def getSource(url):
    html = requests.get(url)

urls = []

for i in range(1, 21):
    newpage = 'http://tieba.baidu.com/p/3522395718?pn='+str(i)
    urls.append(newpage)

time1 = time.time()
for i in urls:
    print(i)
    getSource(i)
time2 = time.time()
print("单线程耗时："+str(time2-time1))

pool = ThreadPool(4)
time3 = time.time()
results = pool.map(getSource, urls)
pool.close()
pool.join()
time4 = time.time()
print("并行耗时："+str(time4-time3))