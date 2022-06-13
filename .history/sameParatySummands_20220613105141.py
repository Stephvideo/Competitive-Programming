# https://codeforces.com/contest/1352/problem/B

for t in range(int(input())):
    n, k = map(int, input().split())

    if n % 2 == 1 and k % 2 == 0:
        print("NO")
        continue

    if k > n:
        print("NO")
        continue

    ans = []
    inc = 0
    if n % 2 == 1:
        inc = 1
    else:
        inc = 2
    
    n -= (k - 1) * inc

    incList = [inc] * (k-1)

    ans.append(n)
    ans = ans + incList
    print("YES")
    print(*ans)