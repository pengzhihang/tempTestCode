#coding:utf-8
import toolClass
import requests
import json
from selenium import webdriver
import time

googleCode=toolClass.getGoogleCode('NHK4SAHJ3VVQZ5YZ')

print googleCode

firstLoginArgs={"locale":"zh_CN","password":"26e52cfad735dd43d675258b6667b54c","username":"13410448384","geetest_challenge":"68e2cb1362f5965d7fabd8b25acc3f0ej6","geetest_validate":"fa89a4d6d5095bc30b8e08ee0775ac40","geetest_seccode":"fa89a4d6d5095bc30b8e08ee0775ac40|jordan","reqId":"38733bd6f92f49afb4d017c2ac4d6112"}

firstReques=requests.post('http://10.1.1.61:8090/user/login',json=firstLoginArgs)

secondLoginArgs={"locale":"zh_CN","password":"26e52cfad735dd43d675258b6667b54c","username":"13410448384","geetest_challenge":"68e2cb1362f5965d7fabd8b25acc3f0ej6","geetest_validate":"fa89a4d6d5095bc30b8e08ee0775ac40","geetest_seccode":"fa89a4d6d5095bc30b8e08ee0775ac40|jordan","reqId":"38733bd6f92f49afb4d017c2ac4d6112","type":1,"verifyCode":googleCode}

secondReques=requests.post('http://10.1.1.61:8090/user/loginVerification',json=secondLoginArgs)

loginData=json.loads(secondReques.content)
    
wb = webdriver.Chrome()

wb.get('http://10.1.1.61:8090/#/pool')

wb.maximize_window()

js2str=str(json.dumps(loginData['data']))

jsScript = 'localStorage.setItem(\'userToken\',\''+js2str+'\')'

wb.execute_script(jsScript)

wb.refresh()

wb.get('http://10.1.1.61:3391/trade/ETH_BTC')

wb.find_element_by_xpath('//div[./div[@class="btn"]]/div[./span[contains(text(),"数量(ETH)")]]//input').send_keys('100')

wb.find_element_by_xpath('//div[./div[@class="btn"]]//button').click()

time.sleep(2)

wb.quit()


