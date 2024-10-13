su,si=set(),set()
for i in range(int(input())):
    tem=set([int(e) for e in input().split()])
    su=su.union(tem)
    if i==0: si=tem
    else: si=si.intersection(tem)
print(len(su))
print(len(si))