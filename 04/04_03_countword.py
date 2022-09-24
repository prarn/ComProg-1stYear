from curses import A_ALTCHARSET


sol=input()
ans=input()
if len(sol)!=len(ans): print('Incomplete answer')
else:
    count=0
    for tem in range(len(sol)):
        if sol[tem]==ans[tem]:
            count+=1
    print(count)