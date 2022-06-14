def isPal(s):
    rev = s[::-1]

    if s == rev:
        return True
    return False

for t in range(int(input())):
    s = input()

    hour = int(s[0:2])
    min = int(s[3:5])
    x = int(s[5:])
    ans = 0
    s = s[0:6]    
    if isPal(s):
        ans += 1
    print(s)
    #print("hi")
    currTime = ""
    # while currTime != s:
    #     currTime = ""
    #     numHours = x // 60
    #     numMin = x % 60

    #     if min + numMin >= 60:
    #         numHours += 1
        
    #     min = (min + numMin) % 60
    #     hour = (hour + numHours) % 24 
    #     print(hour, min)
    #     if hour < 10:
    #         currTime = '0' + str(hour) + currTime
    #     else:
    #         currTime = str(hour) + currTime
        
    #     currTime = currTime + ':'

    #     if min < 10:
    #         currTime = currTime + '0' + str(min)  
    #     else:
    #         currTime = currTime + str(min)
        
    #     #print(s)
    #     #print(currTime)
        
    #     if isPal(currTime):
            
    #         ans += 1

    print(ans)

