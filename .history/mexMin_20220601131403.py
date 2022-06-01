# https://codeforces.com/problemset/problem/1566/B

T = int(input)

for t in range(T):
    s = input()

    numZeros = s.count('0')

    if numZeros == 0:
        print(0)
        continue

    firstZero = s.find('0')
    lastZero = s.find('0')

    substring = s[firstZero:lastZero]
    if substring.find('1'):
        print(2)
    else:
        print(1)