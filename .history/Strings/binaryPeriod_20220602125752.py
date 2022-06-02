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
        #needed = math.ceil(len(s)/2)
        if s[0] == '0':
            print ("01" * (len(s)/2))
        else:
            print ("10" * (len(s)/2))