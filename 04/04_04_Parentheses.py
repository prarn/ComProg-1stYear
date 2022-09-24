i=input()
s=''
for n in range(len(i)):
    if i[n]=='(':
        s+='['
    elif i[n]==')':
        s+=']'
    elif i[n]=='[':
        s+='('
    elif i[n]==']':
        s+=')'
    else: s+=i[n]
print(s)