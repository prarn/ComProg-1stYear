import math
bd,bm,by,d,m,y = [int(tem) for tem in input().split()]
y=y-543
by=by-543
mon=[31,28,31,30,31,30,31,31,30,31,30,31]
n=0
if ((by%4==0 and by%100!=0) or by%400==0) and bm<=2: n=1
red = sum(mon[bm:])+(mon[bm-1]-bd+1)+n
black = (y-by-1)*365
n=0
if ((y%4==0 and y%100!=0) or y%400==0) and m>=2: n=1
blue = sum(mon[:m-1])+d+n-1
t=red+black+blue
a1=math.sin((2*math.pi*t)/23)
a2=math.sin((2*math.pi*t)/28)
a3=math.sin((2*math.pi*t)/33)
print(t,"{:.2f}".format(a1),"{:.2f}".format(a2),"{:.2f}".format(a3))