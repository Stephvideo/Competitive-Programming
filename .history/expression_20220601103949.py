# https://codeforces.com/problemset/problem/479/A

a = int(input())
b = int(input())
c = int(input())

max = 0
curr = (a + b) * c
if curr > max:
    max = curr

curr = (a * b) + c
if curr > max:
    max = curr

curr = a + (b * c)
if curr > max:
    max = curr

curr = a * (b + c)
if curr > max:
    max = curr

print (max)