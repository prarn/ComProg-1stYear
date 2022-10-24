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
    l_amt=list()
    for k in sorted(pocket.items(), key=lambda x: x[0], reverse=True):
        if amt//k[0]>0:
            if (amt//k[0])>k[1]:
                l_amt+=[[k[0],k[1]]]
                amt-=k[1]*k[0]
            else:
                l_amt+=[[k[0],amt//k[0]]]
                amt%=k[0]
    for j in l_amt: pocket[j[0]]-=j[1]
    return {e[0]:e[1] for e in l_amt}
    # amtd=dict()
    # for k in pocket:
    #     if amt//k>0: 
    #         if (amt//k)>pocket[k]:
    #             amtd[k]=pocket[k]
    #             amt-=pocket[k]*k
    #         else: 
    #             amtd[k]=amt//k
    #             amt%=k
    # for i in amtd:
    #     if amtd[i]>pocket[i]: return {}
    # for i in amtd: pocket[i]-=amtd[i]
    # return amtd
exec(input().strip())