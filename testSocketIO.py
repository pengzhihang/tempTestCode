#coding:utf-8
import socketio
import threading
import ssl
ssl.match_hostname = lambda cert, hostname: True

def openSocket():
    
    sio=socketio.Client()
    
    @sio.event
    def connect():
        print 'connecting'
    
    @sio.event
    def message(data):
        print('message received with ', data)
        sio.emit('my response', {'response': 'my response'})
    
    @sio.event
    def disconnect():
        print 'disconnect'
        
    @sio.on('tick')
    def printTick(res):
        print res
        
    @sio.on('kline')
    def printKline(res):
        print res
        
    @sio.on('snapshot')
    def printSnapshot(res):
        print res
        
    @sio.on('indicator_list')
    def printIndicator_list(res):
        print res
        
    @sio.on('exchange')
    def printExchange(res):
        print res
        
    @sio.on('price')
    def printPrice(res):
        print res
        
    setHeaders={'Connection':'Upgrade','Upgrade':'websocket'}
    sio.connect('wss://socket.citex.io/socket.io/?EIO=3&transport=websocket', headers=setHeaders, transports='websocket')
    
    # WS_URL = "wss://socket.citex.io/socket.io/?EIO=3&transport=websocket"
#     netstat -aon | find /c "47.91.148.126"
    
    a='42["subscribe",{"args":[{"topic":"indicator_list"},{"topic":"exchange"},{"topic":"price"}]}]'
    b='42["subscribe",{"args":[{"topic":"snapshot","params":{"contractId":16,"depth":30}},{"topic":"tick","params":{"contractId":16}}]}]'
    c='42["subscribe",{"args":[{"topic":"kline","params":{"contractId":16,"range":"86400000"}}]}]' 
    
    sio.emit('subscribe',a)
    sio.emit('subscribe',b)
    sio.emit('subscribe',c)
    
    sio.wait()

openSocket()