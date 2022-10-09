def a(s):
    s+='$'
    ls=sorted([s[-(i+1):]+s[:-(i+1)] for i in range(len(s))])
    result=''
    for j in ls: result+=j[-1]
    # for k in ls: print(k)
    return result

def o(s):
    s+='$'
    ls=sorted([s[-(i+1):]+s[:-(i+1)] for i in range(len(s))])
    s1,s2='',''
    for j in ls: s2+=j[-1]
    for k in ls: s1+=k[0]
    return [s1,s2]

def t(s):
    ts=[]
    for i in s: ts+=[i+str([e[0] for e in ts].count(i)+1)] 
    return ts

def ao(s1,s2):
    ts1,ts2=t(s1),t(s2)
    result=''
    i=ts1.index('$1')
    while len(result)!=len(s1):
        result+=ts2[i][0]
        i=ts1.index(ts2[i])
    return result[::-1]

x=o('NeverGiveYouUp')
print(ao(x[0],x[1]))