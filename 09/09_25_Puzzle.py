def row_number(t,e):
    for i in range(len(t)):
        if e in t[i]:
            return i

def flatten(t):
    return [ int(e) for i in t for e in i if e!=0]

def inversions(x):
    c=0
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i]>x[j]: c+=1
    return c

def solvable(t):
    n_row=len(t)
    n_inv=inversions(flatten(t))
    n0=row_number(t,0)
    if n_row%2!=0 and n_inv%2==0: return True
    elif n_row%2==0:
        if n_inv%2!=0 and n0%2==0: return True
        elif n_inv%2==0 and n0%2!=0: return True
    return False

exec(input().strip())
# print(row_number([[0,8,7],[6,5,4],[3,2,1]],0))
# print(flatten([[0,8,7],[6,5,4],[3,2,1]]))
# print(inversions(flatten([[0,8,7],[6,5,4],[3,2,1]])))
# print(solvable([[0,8,7],[6,5,4],[3,2,1]]))