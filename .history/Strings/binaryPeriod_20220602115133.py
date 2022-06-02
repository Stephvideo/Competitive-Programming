# https://codeforces.com/problemset/problem/1342/B
import math
for t in range(int(input())):
    s = input()

    same = True
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            same = False
            break
    
    if same:
        print(s)
    else:
        if s[0] == 0:
            needed = math.ceil(len(s)/2)
            print ("01" * needed)
