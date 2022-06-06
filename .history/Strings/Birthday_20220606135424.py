# https://codeforces.com/problemset/problem/1131/C
def getScore(nums):
    score = abs(nums[-1] - nums[0]) 
    for i in range(len(nums)-1):
        if abs(nums[i+1] - nums[i]) > score:
            score = abs(nums[i+1] - nums[i])
    return score

n = int(input())

nums = list(map(int, input().split()))

nums = sorted(nums)


ans = []
ans.append(nums[n-1])

for i in range(n-2, -1, -2):
    if i == 0:
        ans = [nums[i]] + ans
        break
    else:
        ans = [nums[i]] + ans
        ans = ans + [nums[i-1]]

        score = getScore(nums)

        swapped = ans
        swapped[0], swapped[-1] = swapped[-1], swapped[0]
        if getScore(swapped) < score:
            ans = swapped
    
    

print (*ans)