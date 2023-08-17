def knows(r,x,y):
    return y in r[x]
def is_celeb(r,x):
    return (r[x]==set() or r[x]=={x}) and [i for i in r if x not in r[i] and i!=x]==[]
def find_celeb(r):
    for x in r:
        if is_celeb(r,x): return x
    return None
def read_relations():
    r=dict()
    while True:
        d=input().split()
        if len(d)==1: break
        if d[0] not in r: r[d[0]]={d[1]}
        else: r[d[0]].add(d[1])
        if d[1] not in r: r[d[1]]=set()
    return r
def main():
    r=read_relations()
    c=find_celeb(r)
    print(c if c else 'Not Found')
exec(input().strip())