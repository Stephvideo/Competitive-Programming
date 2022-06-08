# https://codeforces.com/problemset/problem/579/A

x = int(input())
xBin = bin(x)
print(type(xBin))
while xBin[-1] == '0':
    xBin >> 1

    #xBin = xBin[0:len(x)]

print(x)