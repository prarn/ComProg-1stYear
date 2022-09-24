line=int(input())
q=list()
t_begin=list()
t_diff=list()
ans=list()
for k in range(line):
    c = input().split()
    if c[0]=='reset': n=int(c[1])
    elif c[0]=='new':
        q.append(n)
        n+=1
        t_begin.append(int(c[1]))
        ans.append('ticket '+str(q[-1]))
    elif c[0]=='next': 
        tem_q=q.pop(0)
        tem_t=t_begin.pop(0)
        ans.append('call '+str(tem_q))
    elif c[0]=='order':
        tt_diff=int(c[1])-tem_t
        t_diff.append(tt_diff)
        ans.append('qtime '+str(tem_q)+' '+str(tt_diff))
    elif c[0]=='avg' or c[0]=='avg_qtime':
        avg=sum(t_diff)/len(t_diff)
        ans.append('avg_qtime '+str(round(avg,4)))
for x in range(len(ans)): print(ans[x])