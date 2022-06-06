# https://codeforces.com/problemset/problem/1131/C

n = int(input())

nums = list(map(int, input().split()))

nums = sorted(nums)


ans = [0] * n

i = n -1
while i//2 > 0:
    ans[i//2] = nums[i]
    ans[i//2 - 1] = nums[i-1]
    ans[i//2 + 1] = nums[i+1]


print (*ans)