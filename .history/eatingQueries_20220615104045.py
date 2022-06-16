# https://codeforces.com/problemset/problem/1676/E

for t in range(int(input())):
    n, q = map(int, input().split())

    lst = list(map(int, input().split()))
    queries = []

    for i in range(q):
        queries.append(int(input()))    

    lst.sort()

    preSum = [lst[0]]

    for i in range(1, n):
        preSum.append(preSum[i-1] + lst[i])

    ans = [-1] * q
    for j in range(q):

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
                
                if check >= queries[j]:
                    if ans[j] == -1:
                        ans[j] = mid - i + 1
                    else:
                        if ans[j] > mid - i + 1:
                            ans[j] = mid - i + 1
                    high = mid - 1
                else:
                    low = mid + 1
        
                
    for i in range(len(ans)):
        print(ans[i])