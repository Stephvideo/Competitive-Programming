# https://codeforces.com/problemset/problem/579/A

x = int(input())
xBin = bin(x)
#print(type(xBin)
ans = 0
for i in xBin:
    if x == '1':
        ans += 1

print (ans)