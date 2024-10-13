n=int(input())
tem_d=dict()
for i in range(n):
    tem=input().split(', ')
    time=tem[3].split(':')
    if tem[2] in tem_d: tem_d[tem[2]]+=int(time[0])*60+int(time[1])
    else: tem_d[tem[2]]=int(time[0])*60+int(time[1])
sorted_d=sorted([ [v,k] for k,v in tem_d.items()],reverse=True)
for e in sorted_d[:3]: print(str(e[1]),'-->',str(e[0]//60)+':'+'0'*(2-len(str((e[0]%60))))+str(e[0]%60))