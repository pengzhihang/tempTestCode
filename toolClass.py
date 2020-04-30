#coding:utf-8
import requests
import json
import time
import sys
import hmac, base64, struct, hashlib, time
 
def getGoogleCode(secretKey):
    input = int(time.time())//30
    key = base64.b32decode(secretKey)
    msg = struct.pack(">Q", input)
    googleCode = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(googleCode[19]) & 15
    googleCode = str((struct.unpack(">I", googleCode[o:o+4])[0] & 0x7fffffff) % 1000000)
    if len(googleCode) == 5:
        googleCode = '0' + googleCode
    return googleCode   

env=1

if env==1:
    url='http://10.1.1.61:8090/'
elif env==2:
    url='https://pre.citex.io/'
elif env==3:
    url='https://www.citex.io/'
else:
    print '获取语言类型错误'

#1、 获取美元，人民币兑率 

getLegalRateRequest=requests.get(url+'common/exchange/list')
legalRateData=json.loads(getLegalRateRequest.content)
def getLegalRate(name):
    for i in legalRateData['result']:
        if i['name']==name:
            Rate=float(i['rate'])
    return Rate
    
# 2、获取币种美元汇率价格

getCurrencyRateRequest=requests.get(url+'common/exchange/coins')
currencyRateData=json.loads(getCurrencyRateRequest.content)
def getCurrencyRate(currencyId):
    for i in currencyRateData['result']:
        if i['currencyId']==int(currencyId):
            coinsRate=float(i['latest'])
            return coinsRate
 
currenryID=3
 
currenryNum=50

 
print '折算人民币价格:'+str(getLegalRate('CNY')*getCurrencyRate(currenryID)*currenryNum)
 
print '折算美元价格:'+str(getLegalRate('USD')*getCurrencyRate(currenryID)*currenryNum)
 
print '折算越南盾价格:'+str(getLegalRate('VND')*getCurrencyRate(currenryID)*currenryNum)
 
print '折算韩元价格:'+str(getLegalRate('KRW')*getCurrencyRate(currenryID)*currenryNum)
