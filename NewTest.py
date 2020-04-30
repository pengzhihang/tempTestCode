#coding:utf-8
import websocket
import gzip
from io import BytesIO
import chardet
import threading

# 接收返回消息
def on_message(ws, message):
    
    getType=chardet.detect(message)
    if getType['encoding']=='ascii':
        print message
    else:
        fdata=BytesIO(message)
        fdata.seek(1)
        with gzip.GzipFile(fileobj=fdata) as f:
            result = f.read()
        print result
        
# 运行错误输出
def on_error(ws, error):
    print '=============运行错误============='
    print error
    
#关闭调用重连
def on_close(ws):
    print '=============连接关闭============='
    connectCitex()
    print '=============重新连接============='
    
#连接开始发送订阅消息
def on_open(ws):
    
    a='42["subscribe",{"args":[{"topic":"indicator_list"},{"topic":"exchange"},{"topic":"price"}]}]'
    b='42["subscribe",{"args":[{"topic":"snapshot","params":{"contractId":16,"depth":30}},{"topic":"tick","params":{"contractId":16}}]}]'
    c='42["subscribe",{"args":[{"topic":"kline","params":{"contractId":16,"range":"86400000"}}]}]' 
    ws.send(a)
    ws.send(b)
    ws.send(c)
    
def connectCitex():
    ws = websocket.WebSocketApp("wss://socket.citex.io/socket.io/?EIO=3&transport=websocket",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              on_open = on_open)
    ws.run_forever(ping_interval=60, ping_timeout=25)
    
for i in range(2):
    t=threading.Thread(target=connectCitex, args=())
    t.start()

