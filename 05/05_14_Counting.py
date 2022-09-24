l=[int(tem) for tem in input().split()]
count=0
for i in range(1,len(l)-1):
    if l[i-1]<l[i]>l[i+1]: count+=1
print(count)