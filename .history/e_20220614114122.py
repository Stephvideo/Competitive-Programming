for t in range(int(input())):
    n, s = map(int, input().split())

    lst = list(map(int, input().split()))

    front = 0
    last = n-1
    ans = 0
    numOnes = lst.count(1)
    if numOnes < s:
        print(-1)
        continue

    flag = False
    while numOnes > s:
        
        if front == last:
            break
        if lst[front] != lst[last]:
            if lst[front] == 1:
                front += 1
                ans += 1
                numOnes -= 1
                continue
            else:
                last -= 1
                ans += 1
                numOnes -= 1
                continue
        if lst[front] == 1: # both eles are 1
            zerosFront = 0
            zerosLast = 0
            for i in range(front+1, last):
                if lst[i] != 0:
                    break
                zerosFront += 1

            for i in range(last-1, front, -1):
                if lst[i] != 0:
                    break
                zerosLast += 1
            # if lst[front] == 0: zerosFront += 1
            # if lst[last] == 0: zerosLast += 1
            
            if zerosFront < zerosLast:
                # if lst[front] == 1:
                numOnes -= 1
                ans += 1
                front += 1
                continue
            else:
                #if lst[last] == 1:
                numOnes -= 1
                ans += 1
                last -= 1
                continue
        else:
            zerosFront = 0
            zerosLast = 0
            for i in range(front, last):
                if lst[i] != 0:
                    break
                zerosFront += 1

            for i in range(last, front, -1):
                if lst[i] != 0:
                    break
                zerosLast += 1

            if zerosFront < zerosLast:
                # if lst[front] == 1:
                front += zerosFront
                ans += zerosFront
                continue
            else:
                #if lst[last] == 1
                last -= (zerosLast)
                ans += zerosLast
                continue
                
    if numOnes == s:
        flag = True
    if flag:
        #print(*lst[front:last+1])
        print(ans)
    else:
        print(-1)