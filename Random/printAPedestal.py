# https://codeforces.com/contest/1690/problem/A
for t in range(int(input())):
    n = int(input())

    peds = [0] * 3
    
    while n > 0:
        if peds[1] == 0:
            peds[1] += 1
            n -=1
        elif peds[0] == 0:
            peds[0] += 1
            n -= 1
        elif peds[2] == 0:
            peds[2] += 1
            n -= 1

        elif peds[2] + 2 <= peds[0]:
            peds[2] += 1
            n -= 1

        elif peds[0] + 2 <= peds[1]:
            peds[0] += 1
            n -= 1
        else:
            peds[1] += 1
            n -= 1

        

    print (*peds)