def lo(n):
    return 10**n
i = float(input())
u=0
while True:
    if i//(lo(u))==0: break
    else: u+=1
l=u-1
while not((lo(u)-lo(l))<=lo(-5)):
    k=(l+u)/2
    if (lo(k))>i:
        u=k
    elif (lo(k))<i:
        l=k
    elif (lo(k))==i:
        break
print(round(k,6))