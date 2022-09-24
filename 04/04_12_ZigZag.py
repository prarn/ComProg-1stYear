i=int(input())
l,r=[],[]
for n in range(i):
    t1,t2=[int(tem) for tem in input().split()]
    if n%2==0: 
        l.append(t1)
        r.append(t2)
    else:
        l.append(t2)
        r.append(t1)
z=input()
if z=='Zig-Zag':
    print(min(l),max(r))
elif z=='Zag-Zig':
    print(min(r),max(l))