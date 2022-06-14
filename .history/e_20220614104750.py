for t in range(int(input())):
    n, s = map(int, input().split())

    lst = list(map(int, input().split()))

    ans = -1
    flag = False
    for i in range(len(lst), -1, -1):
        if flag:
            break
        for j in range(0, len(lst) - i + 1):
            check = lst[j:j+i]
            numOnes = 0
            if j == 0:
                numOnes = check.count(1)
            else:
                if lst[j-1] != lst[j+i-1]:
                    if lst[j-1] == 1:
                        numOnes -= 1
                    else:
                        numOnes += 1
            if numOnes == s:
                flag = True
                ans = len(lst) - i
                break
            
    if flag:
        print(ans)
    else:
        print(-1)