# https://codeforces.com/problemset/problem/1632/B

for t in range(int(input())):
    n = int(input())

    length = len(bin(n)[2:])

    ans = []

    ans.append(2 ** (length-1))
    print("curr: ", 2 ** (length -1))
    curr = (2 ** length-1) + 1
    while curr < n:
        ans.append(curr)
        curr += 1
    
    ans = [0] + ans

    beginning = [i for i in range(1, 2 ** (length -1))]

    ans = beginning + ans

    print (*ans)