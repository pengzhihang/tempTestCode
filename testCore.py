# -*- coding:utf-8 -*-

import zmq
import json
import time

pub_context = zmq.Context()
pub_socket = pub_context.socket(zmq.SUB)
pub_socket.connect("tcp://192.168.1.1:20051") # ÐÐÇé
pub_socket.setsockopt_string(zmq.SUBSCRIBE, "")
while True:
    message = pub_socket.recv().decode('utf-8')
    data = json.loads(message)
    if data['message_type'] == 7:
        print(data, time.time())