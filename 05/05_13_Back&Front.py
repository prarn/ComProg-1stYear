n=int(input())
l1=[]
l3=[]
for q in range(n): l1.append(int(input()))
l2=([int(e) for e in input().split()])
while True:
    tem=int(input())
    if tem == -1: break
    else: l3.append(tem)
tl=l1+l2+l3
if len(tl)%2==0: print(tl[-1:0:-2]+tl[::2])
else: print(tl[-2:0:-2]+tl[::2])