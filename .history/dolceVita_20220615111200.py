# https://codeforces.com/problemset/problem/1671/C

for t in range(int(input())):

    n, x = map(int, input().split())

    costs = list(map(int, input().split()))

    #costs = costs[::-1]
    preSum = [costs[0]] * n
    for i in range(1,n):
        preSum[i] = preSum[i-1] + costs[i]
    ans = 0

    day = 0
    while (costs[0] + day <= x):
        low = 0
        high = n-1
        update = 0
        while(high >= low):
            mid = (low + high)//2

            currCost = preSum[mid] + day*(mid+1)

            if currCost <= x:
                low = mid + 1
                update = mid+1
            else:
                high = mid - 1
        ans += update
        print("buying ", update)
        day += 1

    print(ans)