# https://codeforces.com/problemset/problem/1006/C

n = int(input())

nums = list(map(int, input().split()))
ans = 0
for c in range(n -1, -1, -1):
    for a in range(0, c):
        aSum = sum(nums[0:a])
        cSum = sum(nums[c:n])

        print(nums[0:a])
        print(" ")
        print(nums[c:n])
        if aSum == cSum and aSum > ans:
            ans = aSum
            continue
        
        if aSum > cSum:
            break




print(ans)