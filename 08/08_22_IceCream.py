goods=dict([input().split() for _ in range(int(input()))])
sell=dict()
for i in range(int(input())):
    tem=input().split()
    if tem[0] in goods: 
        if tem[0] in sell: sell[tem[0]]+=float(tem[1])*float(goods[tem[0]])
        else: sell[tem[0]]=float(tem[1])*float(goods[tem[0]])
if sell == {}: print('No ice cream sales')
else: 
    print('Total ice cream sales:',str(sum(list(sell.values()))))
    tl=sorted([[v*-1,k] for k,v in sell.items()])
    print('Top sales:', ', '.join([k for v,k in tl if v==tl[0][0]]))