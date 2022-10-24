# data={t1+' '+t2:t3 for _ in range(int(input())) for t1,t2,t3 in (input().split(), )}
td = dict()
for i in range(int(input())): 
    t=input().split()
    td[t[0]+' '+t[1]]=t[2]
    td[t[2]]=t[0]+' '+t[1]
for j in range(int(input())): 
    t=input()
    if t in td: print(t,'-->',td[t])
    else: print(t,'--> Not found')