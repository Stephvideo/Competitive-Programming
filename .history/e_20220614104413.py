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
            if check.count(1) == s:
                flag = True
                ans = len(lst) - i
                break
            
    if flag:
        print(ans)
    else:
        print(-1)