for t in range(int(input())):
    n = input()

    ans = []
    curr = -1
    for i in range(len(n)-1, -1, -1):
        dig = int(n[i])
        curr += 1
        if dig == 0:
            continue

        dig = dig * 10 ** curr
        

        ans.append(dig)
    
    print(*ans)