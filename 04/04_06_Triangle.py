i=int(input())
for n in range(i):
    for m in range(i-n,1,-1):
        print(' ',end='')
    for k in range(1,2*(n+1)):
        if k in [1,2*n+1]: print('*',end='')
        elif n==i-1: print("*",end='')
        else: print(' ',end='')
    print()