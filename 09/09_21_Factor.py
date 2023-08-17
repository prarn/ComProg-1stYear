def factor(n):
    ans=[]
    for i in range(2,n+1):
        if n==0: break
        while n%i==0:
            n=n//i
            tem=[e[0] for e in ans]
            if i not in tem: ans+=[[i,1]]
            else: ans[tem.index(i)][1]+=1
    return ans
exec(input().strip())