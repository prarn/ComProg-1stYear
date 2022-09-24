i = input()
sum = str(int(i[3::7])+int(i[7::5])+10000)
ans = sum[-4:-1:]
a = ["A","B","C","D","E","F","G","H","I","J"]
print(ans+a[(int(ans[0])+int(ans[1])+int(ans[2]))%10])