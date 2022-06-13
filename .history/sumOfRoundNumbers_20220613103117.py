for t in range(int(input())):
    n = input()

    ans = []
    curr = 0
    for i in range(len(n)-1, -1, -1):
        dig = int(n[i])

        dig = dig * 10 ** curr
        curr += 1
        ans.append(dig)
    
    print(*ans)