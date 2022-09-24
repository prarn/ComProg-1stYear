import math
n=int(input())
x,y,ans=[],[],[0]*n
for tem in range(n):
    t=input().split()
    x.append(float(t[0]))
    y.append(float(t[1]))
    ans[tem]=math.sqrt((x[tem]**2)+(y[tem]**2))
lt=sorted(ans)
m=ans.index(lt[2])
print('#'+str(m+1)+': ('+str(x[m])+', '+str(y[m])+')')