n=int(input())
l=['Robert', 'Dick',
'William', 'Bill',
'James', 'Jim',
'John', 'Jack',
'Margaret', 'Peggy',
'Edward', 'Ed',
'Sarah', 'Sally',
'Andrew', 'Andy',
'Anthony', 'Tony',
'Deborah', 'Debbie']
li=[]
for t in range(n):
    i=input()
    li.append(i)
for k in li:
    if k in l:
        if l.index(k)%2==0: print(l[l.index(k)+1])
        else: print(l[l.index(k)-1])
    else: print('Not found')
