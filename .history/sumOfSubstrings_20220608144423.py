# https://codeforces.com/problemset/problem/1691/C

for t in range(int(input())):
    n, k = map(int, input().split())

    s = input()

    ans = 0
    for i in range(1, n-1):
        if s[i] == '1':
            ans += 11
    
    oneFront = False
    oneBack = False
    if s[0] == '1':
        ans += 10
        oneFront = True    
    if s[-1] == '1':
        ans += 1
        oneBack = True

    if oneBack == False:
        for i in range(n-1, 0, -1):
            if s[i] == '1':
                if n-1 - i <= k:
                    ans -= 10
                    k -= n - i
    if oneFront == False:
        for i in range(0, n):
            if s[i] == '1':
                if i <= k:
                    ans -= 1

    print(ans)