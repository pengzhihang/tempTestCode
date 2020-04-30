#coding:utf-8

a=12

b=12
 
current=40
 
picMax=current*(1+0.1)

print '最高价:'+str(picMax)
 
picMin=current*(1-0.1)

print '最低价:'+str(picMin)
 
setNum=10
 
print '单笔成交利率上浮:'+str((picMax-picMin)/(setNum-1)/(picMin+(picMax-picMin)/(setNum-1)*(setNum-2))*100)
 
print '单笔利率下浮:'+str((picMax-picMin)/(setNum-1)/picMin*100)

print '单笔成交数量:'+str((a+b*(1-0.005)/current)/(setNum-1))

print '单笔成交价格:'+str((picMax-picMin)/(setNum-1))

picList=[]

for i in range(0,setNum):
    picList.append(picMin+(picMax-picMin)/(setNum-1)*i)

print picList

print '初始卖出Btc数量:'

buyPic=40.44 
print '反向挂卖单价格:'+str(buyPic+(picMax-picMin)/(setNum-1))


sellPic=41.33
print '反向挂买单价格:'+str(sellPic-(picMax-picMin)/(setNum-1))

print '买入btc数量'+str((a+b*(1-0.005)/current)/(setNum-1)*5)

print '卖出btc数量'+str((a+b*(1-0.005)/current)/(setNum-1)*4)
