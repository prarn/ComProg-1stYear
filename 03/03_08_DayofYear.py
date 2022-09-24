d,m,y=(int(input()) for tem in range(3))
y=y-543
n=0
mon=[31,28,31,30,31,30,31,31,30,31,30,31]
if y%4==0 and y%100!=0 or y%400==0: n=1
print(sum(mon[:m-1])+n+d)