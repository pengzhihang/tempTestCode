#coding=utf-8
import socketio

sio=socketio.Client(randomization_factor=True)

def connect():
    print 'connecting'

def printKline(data):
    print data
    
def printMessage(data):
    print data

sio.connect('http://pt-socket.citex.io:443',transports='websocket')

a='42["subscribe",{"args":[{"topic":"indicator_list"},{"topic":"exchange"},{"topic":"price"}]}]'
b='42["subscribe",{"args":[{"topic":"snapshot","params":{"contractId":16,"depth":30}},{"topic":"tick","params":{"contractId":16}}]}]'
c='42["subscribe",{"args":[{"topic":"kline","params":{"contractId":16,"range":"86400000"}}]}]' 

sio.emit('subscribe',a)
sio.emit('subscribe',b)
sio.emit('subscribe',c)

sio.on('message',printMessage)
sio.on('kline', printKline)
sio.on('connect', connect)

sio.wait()


