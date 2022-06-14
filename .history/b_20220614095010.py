
for t in range(int(input())):
    seen = set()

    lst = list(map(int, input().split()))

    ans = len(lst)
    numSeen = 0
    for i in range(len(lst)):
        if lst[i] not in seen:
            seen.add(lst[i])
            continue
        else:
            print("i:", lst[i])
            numSeen += 1
            

    if numSeen % 2 == 1:
        numSeen += 1
    
    ans -= numSeen
    print(ans)
