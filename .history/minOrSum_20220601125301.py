# https://codeforces.com/problemset/problem/1635/A

T = int(input())

for t in range(T):
    n = int(input())

    lst = list(map(int, input().split()))

    ans = lst[0]
    for i in range(1, len(lst)):
        ans |= lst[i]

    print(ans)