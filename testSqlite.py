#coding:utf-8
from lxml import etree
import re
import requests
import sqlite3
from concurrent.futures import ThreadPoolExecutor

def insertMagent(htmlNum,title):
    
    conn=sqlite3.Connection('d:\\test.db')

    cur=conn.cursor()
    
    req=requests.get('http://www.nnbb22.com%s'%(htmlNum),timeout=20)
    
    reStr='magnet:\?xt=urn:btih:[0-9a-fA-F]{40}'
    
    magnete=re.search(reStr, req.content).group(0)
    
    sql='INSERT INTO "main"."magnet"("magnet", "title", "url") VALUES ("%s", "%s", "%s");'%(magnete,title,htmlNum)
    
    cur.execute(sql)
    
    conn.commit()
    
    conn.close
    
tl=ThreadPoolExecutor(100)

for i in range(1,266):    
    print i
    urlGet=requests.get('http://www.nnbb22.com/krt35/41/%s.html'%(i))
    getHtml=etree.HTML(urlGet.content)
    urlList=getHtml.xpath("//div[@class='zxlist']//ul/li/a")
    for j in urlList:
        tl.submit(insertMagent,j.get('href'),j.text)
        print j.get('href')
