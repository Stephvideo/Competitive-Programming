# https://codeforces.com/problemset/problem/579/A

x = int(input())
xBin = str(x)

while xBin[-1] == '0':
    x >> 1

    x = x[0:len(x)]

print(x)