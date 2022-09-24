def is_prime(n):
    if n<=1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k==0:
            return False
    return True

def next_prime(n):
    # n+=1
    # while not is_prime(n): n+=1
    # return n
    if is_prime(n+1):
        return n+1
    else:
        return next_prime(n+1)

def next_twin_prime(n):
    # tem=list()
    # while True:
    #     n+=1
    #     if is_prime(n):
    #         tem+=[n]
    #         if len(tem)==2:
    #             if tem[1]-tem[0]==2: 
    #                 return (tem[0], tem[1])
    #             else: tem.pop(0)
    t = next_prime(n+1)
    if next_prime(t)-t==2: return (t, t+2)
    return next_twin_prime(next_prime(t))

exec(input().strip())