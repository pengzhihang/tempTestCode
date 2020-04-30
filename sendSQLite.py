#coding:utf-8
import requests
import sqlite3
import time

connection=sqlite3.connect('d:\\test.db')

    
# for item in range(0,8):
#     
#     cursor=connection.cursor()
#     
#     sql = "SELECT * FROM main.magnet mm LIMIT %s,1000;"%(item)
#     
#     cursor.execute(sql)
#     
#     result = cursor.fetchall()
#     
#     resultList=[]
#     
#     for i in result:
#         global resultList
#         resultList.append([i[1],i[2].encode('utf-8')])
#         
#     print resultList

cursor=connection.cursor()
 
sql = "SELECT * FROM main.magnet mm LIMIT 0,1000;"
 
cursor.execute(sql)
 
result = cursor.fetchall()

resultList=[]

for i in result:
    
    resultList.append(i[2])
       
for i in resultList:
    
    print i

# postUrl="https://sc.ftqq.com/SCU11653Tbb41ab3e084b263443c485a677d3705559b5fe1344043.send"
#   
# postData={"text":"种子列表","desp":str(resultList)}
#   
# postRequest=requests.post(postUrl,data=postData)


