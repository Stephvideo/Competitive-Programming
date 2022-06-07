
# https://codeforces.com/contest/1690/problem/C
from collections import deque

for t in range(int(input())):
    n = int(input())

    enter = list(map(int, input().split())) 
    finish = list(map(int, input().split())) 
    appended = [False] * n
    queue = deque()
    ans = []

    start = 0
    #queue.append(finish[0])
    for i in range(n):
        start = enter[i]
        #print("i", i,  "queue", queue)
        if len(queue) == 0:
            #print("finish", i, " ", finish[i])
            queue.append(finish[i])
            appended[i] = True
        fin = queue.popleft()

        #print("i", i, "fin ", fin, "start ", start)
        
        ans.append(fin - start)
        #print("curr i: ", i)
        
        if i+1 < n and enter[i+1] <= fin:
            #print("element ", j, "was updated from ", enter[j], "to ", fin)
            if not appended[i+1]:
                queue.append(finish[i+1])
                appended[i+1] = True
            enter[i+1] = fin
    #print(*enter)
    #print(*finish)
    print(*ans)    

