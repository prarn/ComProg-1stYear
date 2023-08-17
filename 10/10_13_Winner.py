s1,s2=set(),set()
for i in range(int(input())):
    tem=input().split()
    s1.add(tem[0])
    s2.add(tem[1])
print(sorted(list(s1-s2)))