def read_matrix():
    m=[]
    nrows=int(input())
    for k in range(nrows):
        x=input().split()
        r=[float(e) for e in x]
        m.append(r)
    return m

def mult_c(c,A):
    # for i in range(len(A)):
    #     for j in range(len(A[i])):
    #         A[i][j]*=c
    return [[j*c for j in i]for i in A]

def mult(A,B):
    ans=list()
    for i in range(len(A)):
        tem_ans=[0]*(len(B[0]))
        for j in range(len(B[0])):
            tem=0
            for k in range(len(B)):
                tem+=A[i][k]*B[k][j]
            tem_ans[j]+=tem
        ans+=[tem_ans]
    return ans

exec(input().strip())