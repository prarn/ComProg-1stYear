n=int(input())
l=[]
while n != 1:
    l.append(str(n))
    if n % 2 ==0 : n = n // 2
    else: n = 3*n + 1
l.append('1')
print('->'.join(l[-15:]))