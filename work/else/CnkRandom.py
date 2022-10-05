import random

from sqlalchemy import true

def CnK(n, k):
    l = []
    end = []
    for i in range(1, n+1):
        l.append(i)
    for _ in range(k):
        end.append(l[random.randint(0, k)])
    return end


    
def RandomCnk(c, k):
    table = []
    for _ in range(c*100):
        tmp = -1
        flag = False
        ans = CnK(c, k)
        for i in table:
            if i == ans:
                flag = true
                break
        for i in ans:
            if flag:
                break
            if tmp < i:
                tmp = i
            else:
                flag = true
                break
        if flag:
            continue

        table.append(ans)
    return table

print(RandomCnk(3,2))
