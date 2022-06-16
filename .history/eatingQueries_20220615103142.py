# https://codeforces.com/problemset/problem/1676/E

for t in range(int(input())):
    n, q = map(int, input().split())

    lst = list(map(int, input().split()))

    lst.sort()

    preSum = [lst[0]]

    for i in range(1, n):
        preSum.append(preSum[i-1] + lst[i])

    ans = -1
    for i in range(n):
        low = i
        high = n-1

        while high >= low:
            mid = (high + low)//2
            check = 0

            if i == 0:
                check = preSum[mid]
            else:
                check = preSum[mid] - preSum[i]
            
            if check >= q:
                if ans == -1:
                    ans = mid - i + 1
                elif ans > mid - i + 1:
                    ans = mid - i + 1
                
                high = mid -1
            else:
                low = mid + 1
                
    if ans == -1:
        print(-1)
    else:
        print(ans)