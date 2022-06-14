for t in range(int(input())):
    input()
    flag = False
    ans = []
    for i in range(8):
        s = input()
        #print(s)
        if i == 0:
            continue
        if flag:
            continue
        
        
        found = -1
        mult = False
        for j in range(len(s)):
            if s[j] == '#':
                if found != -1:
                    mult = True
                    break
                found = j
        if not mult:
            ans.append(i+1)
            ans.append(found+1)
            flag = True


    print(*ans)