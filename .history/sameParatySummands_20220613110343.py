# https://codeforces.com/contest/1352/problem/B

for t in range(int(input())):
    n, k = map(int, input().split())

    if n % 2 == 1 and k % 2 == 0:
        print("NO")
        continue

    if k > n:
        print("NO")
        continue
    flag = False
    ans = []
    inc = 1
    check = n
    
    check -= (k - 1) * inc
    if check % 2 == 1:
        ans.append(check)
        incList = [inc] * (k-1)
        ans = ans + incList
        flag = True
    
    if not flag:
        inc = 2
        check = n
        check -= (k-1) * inc

        if check % 2 == 0 and check > 0:
            ans.append(check)
            incList = [inc] * (k-1)
            ans = ans + incList
            flag = True
    
    if flag:
        print("YES")
        print(*ans)
    else:
        print("NO")