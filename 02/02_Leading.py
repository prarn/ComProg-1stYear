m = input()
n = int(input())
s = [0]*n
s[-(len(m)):] = m
print(*s, sep="")