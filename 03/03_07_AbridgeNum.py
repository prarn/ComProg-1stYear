i=int(input())
l=len(str(i))-1
if l<3: print(i,end='')
elif l%3==0 and l<10: print(round(float(i/(10**(l))),1),end='')
elif 3<l<=5: print(round(i/1e3),end='')
elif 6<l<=8: print(round(i/1e6),end='')
elif 9<l: print(round(i/1e9),end='')
if 3<=l<=5: print('K')
elif 6<=l<=8: print('M')
elif 9<=l: print('B')