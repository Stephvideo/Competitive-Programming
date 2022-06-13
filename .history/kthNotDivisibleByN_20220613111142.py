# https://codeforces.com/contest/1352/problem/C

for t in range(int(input())):
    n, k = map(int, input().split())

    if k > n:
        print(k)
        continue
    if k == n:
        print(n + 1)
        continue
    
    print("not implemented")