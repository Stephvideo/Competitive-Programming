for t in range(int(input())):
    input()
    flag = False
    ans = []
    mult = False
    for i in range(8):
        s = input()
        #print(s)
        if flag:
            continue
        
        pounds = []
        for j in range(len(s)):
            if s[j] == '#':
                pounds.append(j+1)
        if not mult:
            if len(pounds) > 1:
                mult = True
        else:
            if len(pounds) == 1:
                ans.append(i+1)
                ans.append(pounds[0])
                #print("hi")
                print(*ans)
                flag= True
            


    