a,b,c,d = [float(tem) for tem in input().split()]
if a<b: a,b=b,a
if c<d: c,d=d,c
if a>=c: n1=c
else: n1=a
if b<=d: n2=d
else: n2=b
print(round(((n1+n2)/2),2))