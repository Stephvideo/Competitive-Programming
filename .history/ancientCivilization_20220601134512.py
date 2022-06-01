# https://codeforces.com/problemset/problem/1625/A


T = int(input())

for t in range(T):
    n, l = map(int, input().split())

    nums = list(map(str, input().split()))

    binNums = ['0'*l] * n
    
    for i in range(len(binNums)):
        nums[i].zfill(l)

        for j in range(l):
            binNums[i][j] = nums[i][j]

    ans = ""
    for i in range(l):
        digSum = 0
        for j in range(len(binNums)):
            if binNums[j][i] == '1':
                digSum +=1
            else:
                digSum -=1

        if digSum >0:
            ans.append('1')
        else:
            ans.append('0')

    print(int(ans, 2)) 

