
for t in range(int(input())):
    seen = {}

    lst = list(map(int, input().split()))

    ans = len(lst)
    numSeen = 0
    for i in range(len(lst)):
        if lst[i] in seen:
            numSeen += 1
        else:
            seen.add(lst[i])

    if numSeen %2 == 1:
        numSeen += 1
    
    ans -= numSeen
    print(ans)
