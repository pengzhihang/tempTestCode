#coding:utf-8

import pymysql.cursors
from datetime import datetime, date
import json
import sys
args=sys.argv
 
class JsonToDatetime(json.JSONEncoder):
    """
    JSONEncoder不知道怎么去把这个数据转换成json字符串的时候，
    它就会调用default()函数，default()函数默认会抛出异常。
    所以，重写default()函数来处理datetime类型的数据。
 
    """
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
 
getConer=pymysql.connect(host='10.1.1.52',user='root',password='Stone@123',db='new_coin_web',port=3306,cursorclass = pymysql.cursors.DictCursor)
 
cur=getConer.cursor()
 
sql = "SELECT nt.CREATE_TIME,nt.CONTENT FROM new_coin_web.t_msg_record nt WHERE nt.CONTACT='%s' ORDER BY nt.CREATE_TIME DESC LIMIT 5"%(args[0])

cur.execute(sql)

desc = cur.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
adb=cur.fetchall()
getConer.close
for i in adb:
    print i['CONTENT'].decode('utf-8').encode('gbk'),i['CREATE_TIME']
# print json.dumps(a,cls=JsonToDatetime)




