# https://codeforces.com/problemset/problem/1682/B

for t in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))

    sortedArr = sorted(arr)
    #print(sortedArr)
    ans = 0
    x = sortedArr[-1]
    correct = True
    while (x > ans):
        for i in range(n):
            if arr[i] == sortedArr[i]: continue

            if arr[i] & sortedArr[i] != x:
                x -= 1
                correct = False
                break 
            else:
                for j in range(i+1, n):
                    if arr[j] == sortedArr[i]:
                        arr[i], arr[j] == arr[j], arr[i] 
        if correct:
            print(x)
            break        
                
    if x == 0:
        print(0)