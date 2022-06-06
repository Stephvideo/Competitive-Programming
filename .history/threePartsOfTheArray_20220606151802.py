# https://codeforces.com/problemset/problem/1006/C

n = int(input())

nums = list(map(int, input().split()))
ans = 0
for c in range(n -1, -1, -1):
    for a in range(0, c):
        aSum = sum(nums[0:a+1])
        cSum = sum(nums[c:n])

        # print(nums[0:a])
        # print(nums[c:n])
        # print("")

        if aSum == cSum and aSum > ans:
            ans = aSum
            continue
        
        if aSum > cSum:
            break




print(ans)