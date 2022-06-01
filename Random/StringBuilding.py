# https://codeforces.com/problemset/problem/1671/A
# O(s), s is length of the string
T = input()

for t in range(int(T)):
    s = input()
    
    printed = False 
    if len(s) == 1:
        print ("NO")
        continue

    current = None
    count = 0
    
   
    for letter in s:
        if current == None:
            current = letter
            count += 1

        elif letter == current:
            count += 1

        else:
            if count == 1:
                print ("NO")
                printed = True
                break
            else:
                current = letter
                count = 1

    if printed == False and count == 1:
        print ("NO")
        continue
    
    if printed == False:
        print ("YES")