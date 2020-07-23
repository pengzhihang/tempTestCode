#coding:utf-8

import time
from selenium import webdriver
'''
Created on 2020-7-23

@author: HP
'''


wb=webdriver.Chrome()

wb.get('https://www.baidu.com')

wb.maximize_window()

time.sleep(5)

wb.quit()