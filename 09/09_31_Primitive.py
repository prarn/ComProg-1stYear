def gcd(a,b):
    while b!=0: a,b=b,a%b
    return a

def is_coprime(a,b,c):
    return gcd(gcd(a,b),gcd(b,c))==1

def primitive_Pythagorean_triples(max_len):
    triple=[]
    for c in range(max_len,2,-1):
        tem=list()
        for b in range(c,2,-1):
            for a in range(b,2,-1):
                if a**2+b**2==c**2 and is_coprime(a,b,c): tem+=[[a,b,c]]
            tem.sort(reverse=True)
        if tem!=[]: triple+=tem
    return triple[::-1]

exec(input().strip())
# print(primitive_Pythagorean_triples(100)[-10:])