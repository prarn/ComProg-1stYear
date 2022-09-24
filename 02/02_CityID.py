i = str(input())
sum = 0
for j in range(len(i)):
    sum += int(i[j]) * (13-j)
iden = (11-((sum) % 11)) % 10
print(i[0]+" "+i[1:5]+" "+i[5:10]+" "+i[10:]+" "+ str(iden))