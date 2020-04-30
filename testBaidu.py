#coding:utf-8

import requests
import re
import json

postData={'grant_type':'client_credentials','client_id':'b51TiGeE0G1c9xtE50kH4hNO','client_secret':'uwTFnekkKUPGzYVvrMxys0lzmC2yhHjR'}
 
rq=requests.post('https://openapi.baidu.com/oauth/2.0/token',data=postData)
 
getToken=json.loads(rq.content)
 
print getToken['access_token']
 
pdata={
    'tex':'肖总,晚上来我们会所玩呀,哈哈哈'.decode('utf-8'),
    'tok':getToken['access_token'],
    'cuid':'ZoharPythonScript',
    'ctp':1,
    'lan':'zh',
    'per':5
    }
 
getData=requests.post('http://tsn.baidu.com/text2audio',data=pdata)
 
with open('d://123.mp3', 'wb') as of:
    of.write(getData.content)
of.close()
# 
# rus=requests.get('https://pt.citex.io/common/queryContract')
# 
# result=json.loads(rus.content)
# 
# commodityResult=result['result']
# 
# errNum=[]
# 
# # 60000(1M),300000(5M),900000(15M),1800000(30M),3600000(1H),14400000(4H),604800000(1D),604800000(1W)
#     
# for i in commodityResult:
#     contractIdNum=i['contractId']
#     rus=requests.get('http://web.citex.vip:10201/quot/queryCandlestick?contractId=%d&range=3600000'%(contractIdNum))
#     result=json.loads(rus.content)
#     resultData=result['data']
#     if len(resultData['lines'])==0:
#         errNum.append(contractIdNum)
#         
# print errNum  

# rs.
# 
# 