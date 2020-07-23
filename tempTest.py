#coding:utf-8

import requests

getHeader={'accept': 'application/json, text/plain, */*',
'accept-currency': 'cny',
'accept-language': 'zh-hans',
'authorization': 'Token T6UZHRWamWZDXhqbFzTqvVLCV2Q5rMQaKzGnsN63',
'referer': 'https://hoo.com/',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

getRE=requests.get('https://hoo.com',headers=getHeader)

print(getRE.text)

