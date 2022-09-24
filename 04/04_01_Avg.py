i = input()
sum,count=0,0
if i=='q': tem=1
else: tem=0
while i!='q':
    sum+=float(i)
    count+=1
    i=input()
if tem: print('No Data')
else: print(round(sum/count,2))