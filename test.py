#coding:utf-8
import websocket
import gzip
from io import BytesIO
import threading
import chardet
import json
import time
import toolClass
import ssl
ssl.match_hostname = lambda cert, hostname: True

def createSocket():
    
    ws=websocket.WebSocket()
    
    wsUrl='wss://socket.citex.io/socket.io/?EIO=3&transport=websocket'
    
#     wsUrl='ws://10.1.1.51:8781/socket.io/?EIO=3&transport=websocket'
    
    # wsUrl='wss://pt-socket.citex.io/socket.io/?EIO=3&transport=websocket'
    
    ws.connect(wsUrl)
    
    contractId=1
    
    range=60000
    
    #订阅消息
    def subscribeMessage():
    
        # 60000(1M),300000(5M),900000(15M),1800000(30M),3600000(1H),14400000(4H),604800000(1D),604800000(1W)
        
        indicator_list='42["subscribe",{"args":[{"topic":"indicator_list"},{"topic":"exchange"},{"topic":"price"}]}]'
        snapshot='42["subscribe",{"args":[{"topic":"snapshot","params":{"contractId":%s,"depth":30}},{"topic":"tick","params":{"contractId":%s}}]}]'%(contractId,contractId)
        kline='42["subscribe",{"args":[{"topic":"kline","params":{"contractId":%s,"range":"%s"}}]}]'%(contractId,range)
        ws.send(indicator_list)
        ws.send(snapshot)
        ws.send(kline)
    
    # 发送心跳消息
    def sendMessage():
        def sendPing():
            ws.send("2")
        while True:
            tim=threading.Timer(25,sendPing)
            tim.start()
            tim.join()
    # 获取返回信息        
    def getMessage():
        t1=False     #最新成交逐条推送
        t2=False     #所有交易对行情
        t3=False     #快照数据
        t4=True     #K线数据   
        while True:
            grs=ws.recv()
            getType=chardet.detect(grs)
            if getType['encoding']=='ascii':
                if 'tick' in grs and t1==True:
                    print '----------------逐条推送订单----------------'
                if 'indicator_list' in grs and t2==True:
                    print '----------------所有交易对行情----------------'
                if 'snapshot' in grs and t3==True:
                    print '----------------快照数据----------------'
                if 'kline' in grs and t4==True:
                    print '----------------K线数据----------------'
            else:
                fdata=BytesIO(grs)
                fdata.seek(1)
                with gzip.GzipFile(fileobj=fdata) as f:
                    result = f.read()
                print result
                jsondata=json.loads(result)
                
    #           最新成交价tick
                if jsondata['topic'] =='tick' and t1==True:
                    getD=jsondata['data']
                    getTrades=getD['trades']
                    getResult=getTrades[0]
                    getNum=getResult[1]
                    getPrice=getResult[2]
                    getTime=getResult[0]/1000000
                    dt = time.strftime("%H:%M:%S",time.localtime(getTime))
                    print '最新成交价：时间：%s ， 数量：%s ， 委托量:%s'.decode('utf-8')%(dt,getNum,getPrice)
                     
                    print '折算人民币价格:  '+str(toolClass.getCurrencyRate(2)*toolClass.getLegalRate('CNY')*float(getNum))
                 
    #           所有交易对indicator_list
                if jsondata['topic']=='indicator_list' and t2==True:
                    for i in jsondata['data']:
                        if i['contractId']==contractId:
                            priceChangeRadio=float(i['priceChangeRadio'])*100
                            if priceChangeRadio>0:
                                priceString='+'+'%.2f'%(priceChangeRadio)+'%'
                            else:
                                priceString='%.2f'%(priceChangeRadio)+'%'
                            print '所有交易对行情：%s , 涨跌幅：%s'.decode('utf-8')%(i['lastPrice'],priceString)
                            print '折算人民币价格:  '+str(toolClass.getCurrencyRate(2)*toolClass.getLegalRate('CNY')*float(i['lastPrice']))
    
    #           快照snapshot
                if jsondata['topic']=='snapshot' and t3==True:
                    orderSheetAsks=jsondata['data']['asks']
                    for i in orderSheetAsks:
                        print i
                    print '上部分为委托卖出订单-------------------'
                    print '下部分为委托买入订单-------------------'
                    orderSheetBids=jsondata['data']['bids']
                    for i in orderSheetBids:
                        print i
                    
    #           K线Kline
                if jsondata['topic']=='kline' and t4==True:
                    for i in jsondata['data']['lines']:
                        print 'K线数据'+str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i[0]/1000)))+'\''+str(i[1])+'\''+'\''+str(i[2])+'\''+'\''+str(i[3])+'\''+'\''+str(i[4])+'\''+'\''+str(i[5])+'\''
    
    
    subscribeMessage()     
    t1=threading.Thread(target=sendMessage, args=())
    t2=threading.Thread(target=getMessage, args=())
    t1.start()
    t2.start()

for i in range(1):
    
    t3=threading.Thread(target=createSocket, args=())
    t3.start()


