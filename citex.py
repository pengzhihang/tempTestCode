#coding:utf-8
import requests
import toolClass
import time
import hashlib
import datetime
import json
import uuid

contractId=[1,2,3,14,15,16,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,1609,1613,1615,1618,1619,1620,1622,1623,1629]



for item in contractId:
    
    def get_time_stamp13():
        
        # 生成13时间戳   eg:1540281250399895
        datetime_now = datetime.datetime.now()
    
        # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
        date_stamp = str(int(time.mktime(datetime_now.timetuple())))
    
        # 3位，微秒
        data_microsecond = str("%06d"%datetime_now.microsecond)[0:3]
    
        date_stamp = date_stamp+data_microsecond
        
        return int(date_stamp)
    
    def getSignature(myString):
        myCode=hashlib.md5()
        myCode.update(myString.encode('utf-8'))
        return myCode.hexdigest()
     
    googleCode=toolClass.getGoogleCode('NU2JZQIYA7L7C6U6')
      
    firstLoginArgs={"locale":"zh_CN","password":"26e52cfad735dd43d675258b6667b54c","username":"13410448384","geetest_challenge":"68e2cb1362f5965d7fabd8b25acc3f0ej6","geetest_validate":"fa89a4d6d5095bc30b8e08ee0775ac40","geetest_seccode":"fa89a4d6d5095bc30b8e08ee0775ac40|jordan","reqId":"38733bd6f92f49afb4d017c2ac4d6112"}
      
    firstReques=requests.post('http://10.1.1.61:8090/user/login',json=firstLoginArgs)
    
    print (firstReques.content)
      
    secondLoginArgs={"locale":"zh_CN","password":"26e52cfad735dd43d675258b6667b54c","username":"13410448384","geetest_challenge":"68e2cb1362f5965d7fabd8b25acc3f0ej6","geetest_validate":"fa89a4d6d5095bc30b8e08ee0775ac40","geetest_seccode":"fa89a4d6d5095bc30b8e08ee0775ac40|jordan","reqId":"38733bd6f92f49afb4d017c2ac4d6112","type":1,"verifyCode":googleCode}
      
    secondReques=requests.post('http://10.1.1.61:8090/user/loginVerification',json=secondLoginArgs)
    
    print (secondReques.content)
    
    getResut=json.loads(secondReques.content)
    
    buyDate={"contractId":item,"side":1,"price":"0.40000000","quantity":"0.1","orderType":"1","timeInForce":"2","uuid":str(uuid.uuid1()),"signCode":getResut['data']['sign_code'],"signTime":get_time_stamp13(),"signature":getSignature(getResut['data']['access_token']+getResut['data']['sign_code']+str(get_time_stamp13()))}
    print (get_time_stamp13())
    
    httpHeand={
    'Accept':'application/json, text/plain, */*',
    'Authorization':'bearer '+str(getResut['data']['access_token'])
    }
    
    buyReques=requests.post('http://10.1.1.61:3391/order/place',json=buyDate,headers=httpHeand)
    print (buyReques.content)
      
    
    sellDate={"contractId":item,"side":-1,"price":"0.400000000","quantity":"0.1","orderType":"1","timeInForce":"2","uuid":str(uuid.uuid1()),"signCode":getResut['data']['sign_code'],"signTime":get_time_stamp13(),"signature":getSignature(getResut['data']['access_token']+getResut['data']['sign_code']+str(get_time_stamp13()))}
    print (get_time_stamp13()) 
    sellReques=requests.post('http://10.1.1.61:3391/order/place',json=sellDate,headers=httpHeand)
    
    print (sellReques.content)
    
