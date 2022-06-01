# https://codeforces.com/problemset/problem/1527/A

T = int(input())

for t in range(T):
    n = int(input())
    k = (2 ** (len(bin(n))-3)) - 1
    print(k)