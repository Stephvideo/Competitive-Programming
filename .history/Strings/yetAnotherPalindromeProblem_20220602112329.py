# https://codeforces.com/problemset/problem/1324/B

def isPalindrome(nums):
    revNums = nums.reverse()

    for i in range(len(nums)):
        if nums[i] != revNums[i]:
            return False
    return True

def getSubSequences(finalList, index, origArray, subArray):
    
    if index == len(origArray):
        if (len(subArray) != 0):
            finalList.append(subArray)
        return subArray
    else:
        finalList.append(getSubSequences(finalList, index + 1, origArray, subArray))

        finalList.append(getSubSequences(finalList, index + 1, origArray, subArray + [origArray[index]]))
        return finalList

T = int(input())

for i in range(T):
    n = int(input())
    nums = list(map(int, input().split()))

    flag = False
    subSequences = []
    subSequences = getSubSequences(subSequences, 0, nums, [])

    for s in subSequences:
        if len(s) >= 3:
            if isPalindrome(s):
                flag = True
                break
        

    if flag:
        print("YES")
    else:
        print("NO")
