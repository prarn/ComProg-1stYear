g=['F','D','D+','C','C+','B','B+','A']
id=[]
idg=[]
while True:
    t=input()
    if t == 'q': break
    else: t1,t2 = t.split()
    id.append(t1)
    idg.append(t2)
n=[ tem for tem in input().split()]
for i in n:
    if i in id and idg[id.index(i)] != 'A': idg[id.index(i)]=g[g.index(idg[id.index(i)])+1]
for j in range(len(id)): print(id[j],idg[j])