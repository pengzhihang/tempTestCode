#coding:utf-8
import requests
import toolClass
import time
import hashlib
import datetime
import json
import uuid

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
  
secondLoginArgs={"locale":"zh_CN","password":"26e52cfad735dd43d675258b6667b54c","username":"13410448384","geetest_challenge":"68e2cb1362f5965d7fabd8b25acc3f0ej6","geetest_validate":"fa89a4d6d5095bc30b8e08ee0775ac40","geetest_seccode":"fa89a4d6d5095bc30b8e08ee0775ac40|jordan","reqId":"38733bd6f92f49afb4d017c2ac4d6112","type":1,"verifyCode":googleCode}
  
secondReques=requests.post('http://10.1.1.61:8090/user/loginVerification',json=secondLoginArgs)

getResut=json.loads(secondReques.content)

httpHeand={
'Accept':'application/json, text/plain, */*',
'Authorization':'bearer '+str(getResut['data']['access_token'])
}

def createOrder(orderList):
    
    for i in orderList:
        
        time.sleep(0.5)
        
        orderDate={"contractId":i[0],"side":i[1],"price":i[2],"quantity":i[3],"orderType":"1","timeInForce":"2","uuid":str(uuid.uuid1()),"signCode":getResut['data']['sign_code'],"signTime":get_time_stamp13(),"signature":getSignature(getResut['data']['access_token']+getResut['data']['sign_code']+str(get_time_stamp13()))}
        
        orderReques=requests.post('http://10.1.1.61:3391/order/place',json=orderDate,headers=httpHeand)
        
        print orderReques.content
        
def selectOrder():
    
    selectOrders=requests.get('http://10.1.1.61:3391/order/queryActiveOrders?contractId=39',headers=httpHeand)
    
    return selectOrders.content
