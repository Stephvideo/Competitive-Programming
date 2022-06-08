# https://codeforces.com/problemset/problem/1559/A

for t in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))

    nums.sort()

    for i in range(n-1):
        change = nums[i] & nums[i+1]

        nums[i] = change
        nums[i+1] = change
    
    print(nums[-1])