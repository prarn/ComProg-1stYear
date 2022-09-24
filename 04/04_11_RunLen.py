i=input()
tem = i[0]
count=0
for n in range(len(i)):
    if i[n]!=tem:
        print(tem,count,end=' ')
        tem=i[n]
        count=0
    count+=1
print(tem,count)