import math
i = input().split(",")
a = int(i[0]+i[1]+i[2])-int(i[0]+i[1])
b = (10 ** len(i[1]+i[2]))-(10 ** len(i[1]))
print(int(a//math.gcd(a,b)),int(a/math.gcd(a,b)))
print(int(a//math.gcd(a,b)),'/',int(b//math.gcd(a,b)))