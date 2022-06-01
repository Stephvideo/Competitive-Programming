# https://codeforces.com/problemset/problem/1566/B

T = int(input())

for t in range(T):
    s = input()

    numZeros = s.count('0')

    if numZeros == 0:
        print(0)
        continue

    firstZero = s.find('0')
    lastZero = s.find('0')
    print("t", t, "firstZero", firstZero, " secondZero:", lastZero)
    #substring = s[firstZero:lastZero]
    #print(t, substring)
    if s.find('1', firstZero, lastZero) != -1:
        print(2)
    else:
        print(1)