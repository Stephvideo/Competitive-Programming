for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    curr = [0] * n

    if n == 1:
        if nums[0] == 0:
            print("YES")
        else:
            print("NO")
        continue

    flag = False
    pointer = 0
    
    if nums[0] <= 0:
        print("NO")
        continue

    # needed = nums[0] - curr[0]

    # curr[0] += needed
    # curr[1] -= (needed - 1)

    pointer = n-1
    walked = False
    while pointer != 0:
        if nums[pointer] == curr[pointer]:
            pointer -= 1
            continue
        else:
            if not walked:
                for i in range(1, pointer):
                    curr[i] += 1
                walked = True

            needed = curr[pointer] - nums[pointer]

            if needed < 0:
                flag = True
                break
            else:
                curr[pointer - 1] += needed -1
                curr[pointer] -= needed
                pointer -=1
    print(*nums)
    print(*curr)
    
    if flag:
        print("NO")        
    else:
        print("YES")
