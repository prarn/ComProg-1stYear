n=input().split()
m=input()
med=len(n)//2
for i in m:
    if i == 'C': n=n[med:]+n[:med]
    elif i == 'S':
        tf=n[:med]
        tb=n[med:]
        n.clear()
        for j in range(med):
            n.append(tf[j])
            n.append(tb[j])
print(' '.join(n))