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

# 13000000000 XW5IIMPANW5OXDYL

# 13200000000 S4U3FIND526JQZQG

# 13300000000 CBROWFFXCZK5MNMO

print getGoogleCode('CBROWFFXCZK5MNMO')