#coding:utf-8

import requests
import json
import time

while True:
    
    time.sleep(2)
    
    re=requests.get('http://10.1.1.61:8090/push/queryClientList')
    
    getDate=json.loads(re.content)
    
    print len(getDate['data'])
    