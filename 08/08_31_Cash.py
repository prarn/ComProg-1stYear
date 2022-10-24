def total(pocket): 
    return sum([k*v for k,v in pocket.items()])
def take(pocket,money_in):
    result=pocket
    for i in money_in:
        if i not in result: result[i]=0
        result[i]+=money_in[i]
    return result
def pay(pocket,amt):
    if amt>total(pocket): return {}
    amtd=dict()
    for k in pocket:
        if amt//k>0: 
            if (amt//k)>pocket[k]:
                amtd[k]=pocket[k]
                amt-=pocket[k]*k
            else: 
                amtd[k]=amt//k
                amt%=k
    for i in amtd:
        if amtd[i]>pocket[i]: return {}
    for i in amtd: pocket[i]-=amtd[i]
    return amtd
exec(input().strip())