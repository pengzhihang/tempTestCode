#coding:utf-8
import createTrade
import json

putUsdtNum=500
usdtGrids=10

putEthNum=50
ethGrids=10

currentPrice=40
maxPrice=currentPrice*(1+0.1)
minPrice=currentPrice*(1-0.1)

print maxPrice,minPrice

buyList=[]
for i in range(usdtGrids):
    buyList.append(minPrice+(currentPrice-minPrice)/usdtGrids*i) 

print '投入买入价格:'+str(buyList)
buyNum=[]

for i in buyList:
    buyNum.append('%.3f'%(putUsdtNum/usdtGrids/(i*(1+0.002))))
    
print '投入买入数量:'+str(buyNum)

buyTosell=[]
for i in buyList:
    buyTosell.append('%.2f'%(i+(currentPrice-minPrice)/usdtGrids))

print '反向挂卖单价格:'+str(buyTosell)

print '----------分隔符----------'

sellList=[]

for i in range(ethGrids):
    sellList.append(maxPrice-(maxPrice-currentPrice)/ethGrids*i) 
    
print '投入卖出价格:'+str(sellList)

print '投入买入数量:'+str('%.6f'%(putEthNum/ethGrids))

sellTobuy=[]

for i in sellList:
    sellTobuy.append('%.2f'%(i-(maxPrice-currentPrice)/ethGrids))
    
print '反向挂买单价格:'+str(sellTobuy)

buyOrders=[]
sellOrders=[]

for i in range(len(buyList)):
    buyOrders.append([39,1,buyList[i],buyNum[i]])

for i in range(len(sellList)):
    sellOrders.append([39,-1,sellList[i],'%.6f'%(putEthNum/ethGrids)])

orderBuy=[]
orderSell=[]

selectResult=json.loads(createTrade.selectOrder())

for i in selectResult['list']:
    if i['side']=='-1':
        orderSell.append([i['contractId'],int(i['side']),float(i['price']),str(i['quantity'])])
    else:
        orderBuy.append([i['contractId'],int(i['side']),float(i['price']),str(i['quantity'])])

print buyOrders
print sellOrders
print orderBuy
print orderSell

# createTrade.createOrder(buyOrders)
# createTrade.createOrder(sellOrders)