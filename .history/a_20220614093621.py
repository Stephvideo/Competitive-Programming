
for t in range(int(input())):
    lst = list(map(int, input().split()))

    ans = 0

    for i in range(1,len(lst)):
        if lst[i] > lst[0]:
            ans += 1

    print(ans)

