# https://codeforces.com/problemset/problem/1625/A


T = int(input())

for t in range(T):
    n, l = map(int, input().split())

    nums = list(map(int, input().split()))

    binNums = ['0'*l] * n
    print (binNums)

