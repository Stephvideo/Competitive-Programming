# 
for t in range(int(input())):
    zeros, ones = map(int, input().split())

    ans = ""
    if zeros < ones:
        while zeros >0:
            ans = ans + "0"
            zeros -= 1
            ans = ans + "1"
            ones -= 1
        
        left = True
        while ones >0:
            if left:
                ans = "1" + ans
                ones -= 1
                left = False
            else:
                ans = ans + "1"
                ones -= 1
                left = True
    else:
        while ones > 0:
            ans = ans + "1"
            ones -= 1
            ans = ans + "0"
            zeros -=1    
        
        
        left = True
        while zeros >0:
            if left:
                ans = "0" + ans
                zeros -= 1
                left = False
            else:
                ans = ans + "0"
                zeros -= 1
                left = True

    print(ans)