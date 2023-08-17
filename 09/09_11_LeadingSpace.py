n=int(input())
for i in range(n):
    s=input()
    if s=='': print(s)
    elif s[0]=='.':
        tem=0
        for j in s:
            if j=='.': tem+=1
            else: break
        print(s[tem//2:])
    else: print(s)