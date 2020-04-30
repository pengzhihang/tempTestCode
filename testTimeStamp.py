#coding:utf-8
# tstime=''
import time
import datetime

timeStamp='158496944200'
times='2020-01-01 00:00:00'
# 时间戳转日期

print time.strptime(times,"%Y-%m-%d %H:%M:%S")


print time.time()

# 日期转时间戳

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))