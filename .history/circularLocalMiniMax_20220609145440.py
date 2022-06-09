# https://codeforces.com/problemset/problem/1685/A

for t in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))
    print("hi")
    arr.sort()
    ans = []
    for i in range(0, n/2):
        ans.append(arr[i])
        ans.append(arr[n/2 + i])

    flag = True
    for i in range(n):
        if i == n-1:
            if ans[i] <= ans[0]:
                flag = False
                break
        else:
            if ans[i] >= ans[i+1]:
                flag = False
                break
    if flag:
        print("YES")
        print(*ans)
    else:
        print("NO")