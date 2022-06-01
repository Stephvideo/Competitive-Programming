# https://codeforces.com/problemset/problem/1625/A


T = int(input())

for t in range(T):
    n, l = map(int, input().split())

    nums = list(map(str, input().split()))

    ans = 0
    for i in range(l):
        pos = 0

        for currNum in nums:
            if 1 & (currNum >> i):
                pos += 1
            else:
                pos -= 1
        
        if pos > 0:
            ans += 2 ** i
    print(ans)

