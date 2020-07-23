#coding:utf-8
import websocket
import time

ws=websocket.WebSocket()

ws.connect('ws://121.40.165.18:8800')

while True:
    
    print (ws.recv())
    time.sleep(2)
    ws.send('hi my name is zohar')
    

