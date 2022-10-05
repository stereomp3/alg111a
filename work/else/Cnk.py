from sqlalchemy import table, true
from torch import le


table = []
isStart = False
def Cnk(n, k, end=[]):
    if len(n) == 0:
        tmp = []
        for i in range(k):
            tmp.append(end[i])    
        
        tmpNum = -1
        for i in tmp:
            if tmpNum < i:
                tmpNum = i
            else:
                return

        if len(table) == 0:
            table.append(tmp)
        if tmp in table:
            return
        else:
            table.append(tmp)
                 
    else:
        for i in range(len(n)):
            # list[n, end, step]
            # Cnk(n[0:i:1] + n[i + 1:len(start):1], end + n[i:i + 1:1])
            Cnk(n[:i] + n[i+1:], k, end + n[i:i+1])

n = [i for i in range(1, 5+1)]            
Cnk(n, 3)
print(table)