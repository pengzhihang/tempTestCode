#coding:utf-8

import time

timeStamp=1595311754.000000

print (time.time())

## 时间戳转日期
print (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))