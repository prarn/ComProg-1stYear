n=input()
d=dict()
al=list()
while n!='q':
    n=n.split(', ')
    if n[1] not in d: 
        d[n[1]]=[n[0]]
        al+=[n[1]]
    else: d[n[1]]+=[n[0]]
    n=input()
for i in al: print(i+':',', '.join(d[i]))