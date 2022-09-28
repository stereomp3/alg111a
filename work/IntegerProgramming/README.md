https://gitlab.com/cccnqu111/alg/-/blob/master/A2-QA/integerProgramming/README.md

解

`max: 7*x1 + 8*x2 + 2*x3 + 9*x4 + 6*x5`

限制條件

```
5*x1 + 7*x2 + 9*x3	+ 2*x4 + 1*x5	≤	250
18*x1 + 4x2 – 9*x3 + 10x4 + 12*x5 ≤ 285
4*x1 + 7*x2 + 3*x3 + 8*x4 + 5*x5 ≤ 211
5*x1 + 13*x2 + 16*x3 + 3x4 – 7*x5 ≤ 315
```



使用[暴力法](#暴力法)、[爬山演算法](#爬山演算法)、[貪婪法](#貪婪法)

## 暴力法

[BruteForce](BruteForce.py): 使用5個for迴圈解

執行結果

```sh
[[7, 21, 0, 2, 4], 259]  # [x, max]
time:0:00:02.267939  # 執行時間
```

最大值為259

```python
from datetime import datetime

coe = [7, 8, 2, 9, 6]

restriction = [[5, 7, 9, 2, 1, 250],
               [18, 4, -9, 10, 12, 285],
               [4, 7, 3, 8, 5, 211],
               [5, 13, 16, 3, -7, 315]]

def f(c, x):
    """
    function(f(x))
    :param C: 填入判斷函數，它會回傳函數的值 (f(x))
    :param x: x列表
    :return: y
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i:
            sum += c[i] * x[i]
    return sum

def brute_force():
    """
    主要破解函式，使用超級暴力，針對5個變數進行for迴圈
    :return: 答案列表
    """
    ans = 0
    x = []
    for x1 in range(70):
        if restraint([x1], restriction) == -100:
                            break
        for x2 in range(70):
            if restraint([x1, x2], restriction) == -100:
                            break
            for x3 in range(70):
                if restraint([x1, x2, x3], restriction) == -100:
                            break
                for x4 in range(70):
                    if restraint([x1, x2, x3, x4], restriction) == -100:
                            break
                    for x5 in range(70):
                        if restraint([x1, x2, x3, x4, x5], restriction) == -100:
                            break
                        NewAns = f(coe, [x1, x2, x3, x4, x5])
                        if ans < NewAns:
                            ans = NewAns
                            x = [x1, x2, x3, x4, x5]
    return [x, ans]


def restraint(x, r):
    """
    限制函式，用來減f(x)，當x的規則不合的時候，就不讓他進入if條件
    :param x: 變動的x
    :param r: 函數的限制條件，使用二維陣列存取，前面是參數，後面是限制數
    :return: 限制的逞罰，-100或是0(無逞罰)
    """
    sum = []
    if not len(r): # 沒有限制條件
        print("no restraction!")
        return 0

    for i in range(len(r)):
        sum.append(0)
        for j in range(len(r[i])-1):
            if len(x) > j: # 如果x比參數少就跳過，防止出錯
                if x[j] < 0:   # x為負數就逞罰
                    return -100
                sum[i] += r[i][j] * x[j]
        if sum[i] > r[i][len(r[i])-1]:  # 判斷基本條件
            return -100 
    return 0      

startTime = datetime.now()
print(brute_force())  # 打印最後結果
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
```





## 爬山演算法

[hillClimbing01](hillClimbing01.py): 使用全部參數一同增長做處理，dx設定為1

執行結果: 

```sh
[[8, 8, 8, 8, 7], 250]  # [x, max]
time:0:00:00.000999   # 執行時間
```

最大值為250

```python
from datetime import datetime

coe = [7, 8, 2, 9, 6]
init_x = [0, 0, 0, 0, 0]

restriction = [[5, 7, 9, 2, 1, 250],
               [18, 4, -9, 10, 12, 285],
               [4, 7, 3, 8, 5, 211],
               [5, 13, 16, 3, -7, 315]]

def hillClimbing(f, x, _dx=1):
    """
    主要爬山函式
    :param f: 填入判斷函數，它會回傳函數的值 (f(x))
    :param x: 初始的位置，會慢慢的變動，直到f(x+dx)<f(x) && f(x-dx)<f(x)，就會跳出迴圈
    :param dx: 用來爬山的位移，函數內定好了
    :return:
    """
    peak = False
    while (not peak):
        for i in range(len(x)):
            tmpA = x.copy()
            tmpD = x.copy()
            tmpA[i] += _dx
            tmpD[i] -= _dx
            if f(coe, tmpA)>f(coe, x) - restraint(tmpA, restriction):
                x = tmpA
            elif f(coe, tmpD)>f(coe, x) - restraint(tmpD, restriction):
                x = tmpD
            else:  # 最後對每個進行最後的運算
                peak = True  # 到頂了，下面會跳出迴圈，給定最大值   
    return [x, ManAns(coe, x)]

def f(c, x):
    """
    主要爬山函式
    :param c: 函數的參數
    :param x: 變動的x
    :return: y
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i:  # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
    return sum

def restraint(x, r):
    """
    限制函式，用來減f(x)，當x的規則不合的時候，就不讓他進入if條件
    :param x: 變動的x
    :param r: 函數的限制條件，使用二維陣列存取，前面是參數，後面是限制數
    :return: 限制的逞罰，-100或是0(無逞罰)
    """
    sum = []
    if not len(r): # 沒有限制條件
        print("no restraction!")
        return 0

    for i in range(len(r)):
        sum.append(0)
        for j in range(len(r[i])-1):
            if len(x) > j: # 如果x比參數少就跳過，防止出錯
                if x[j] < 0:   # x為負數就逞罰
                    return -100
                sum[i] += r[i][j] * x[j] 
        if sum[i] > r[i][len(r[i])-1]:  # 判斷基本條件
            return -100 
    return 0 
    
def ManAns(c, x):
    """
    用來算函數最大值
    :param c: 函數的參數
    :param x: 變動的x
    :return: 傳回函數的最大值
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i: # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
    return sum

startTime = datetime.now()
print(hillClimbing(f, init_x))  # 打印最後結果
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
```



[hillClimbing02](hillClimbing02.py): 使用`random.randint(-_dx,_dx)`爬山，dx設定為10，對每一個x做加上random number的動作，如果找不到更大的值100000次，就代表目前的是最大值，答案是隨機的

下面是一組較好的隨機執行結果

```sh
[[11, 8, 7, 11, 0], 254]   # [x, max]
time:0:00:00.442703   # 執行時間
```

隨機最大值為: 254

```python
import random
from datetime import datetime

coe = [7, 8, 2, 9, 6]
init_x = [0, 0, 0, 0, 0]

restriction = [[5, 7, 9, 2, 1, 250],
               [18, 4, -9, 10, 12, 285],
               [4, 7, 3, 8, 5, 211],
               [5, 13, 16, 3, 7, 315]]
fail_times = 100000

def hillClimbing(f, x, _dx=10):
    """
    主要爬山函式
    :param f: 填入判斷函數，它會回傳函數的值 (f(x))
    :param x: 初始的位置，會慢慢的變動，直到f(x+dx)<f(x) && f(x-dx)<f(x)，就會跳出迴圈
    :param dx: 用來爬山的位移，函數內定好了
    :return:
    """
    fail_count = 0
    while (fail_count < fail_times):
        for i in range(len(x)):
            tmp = x.copy()
            tmp[i] += random.randint(-_dx,_dx)
            if f(coe, tmp)>f(coe, x) - restraint(tmp, restriction):
                x = tmp
                fail_count = 0
            else:  # 最後對每個進行最後的運算
                fail_count += 1

    return [x, ManAns(coe, x)]

def f(c, x):
    """
    主要爬山函式
    :param c: 函數的參數
    :param x: 變動的x
    :return: y
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i:  # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
    return sum

def restraint(x, r):
    """
    限制函式，用來減f(x)，當x的規則不合的時候，就不讓他進入if條件
    :param x: 變動的x
    :param r: 函數的限制條件，使用二維陣列存取，前面是參數，後面是限制數
    :return: 限制的逞罰，-100或是0(無逞罰)
    """
    sum = []
    if not len(r): # 沒有限制條件
        print("no restraction!")
        return 0

    for i in range(len(r)):
        sum.append(0)
        for j in range(len(r[i])-1):
            if len(x) > j: # 如果x比參數少就跳過，防止出錯
                if x[j] < 0:   # x為負數就逞罰
                    return -100
                sum[i] += r[i][j] * x[j]
        if sum[i] > r[i][len(r[i])-1]:  # 判斷基本條件
            return -100 
    return 0      

def ManAns(c, x):
    """
    用來算函數最大值
    :param c: 函數的參數
    :param x: 變動的x
    :return: 傳回函數的最大值
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i: # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
    return sum

startTime = datetime.now()
print(hillClimbing(f, init_x))  # 打印最後結果
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
```







## 貪婪法

貪婪法: 係數最大的開始下手，使用一個列表紀錄權重，係數越大，權重越重，從權重大的開始往上加。但是效果好像不太好(因該是要把restriction的係數也考慮進去)

最後結果如下: 

```sh
[[0, 0, 1, 26, 0], 236]  # [x, max]
time:0:00:00.000999  # 執行時間
```

最大值等於 236

```python
from datetime import datetime

coe = [7, 8, 2, 9, 6]
init_x = [0, 0, 0, 0, 0]

restriction = [[5, 7, 9, 2, 1, 250],
               [18, 4, -9, 10, 12, 285],
               [4, 7, 3, 8, 5, 211],
               [5, 13, 16, 3, -7, 315]]

def greedy(f, x, _dx=1):
    """
    運行貪婪法的主要程式碼
    :param f: 填入判斷函數，它會回傳函數的值 (f(x))
    :param x: 初始的位置，會慢慢的變動，直到f(x+dx)<f(x) && f(x-dx)<f(x)，就會跳出迴圈
    :param dx: 用來爬山的位移，函數內定好了
    :return:
    """
    weight = setWeights(coe)
    max_index = findMaxWeightIndex(weight)
    while (True):
        tmp = x.copy()
        tmp[max_index] += _dx
        
        if f(coe, tmp)>f(coe, x) - restraint(tmp, restriction):
            x = tmp
        else:  
            if not ResetMaxWeight(weight):
                break
            max_index = findMaxWeightIndex(weight) 
                
    return [x, ManAns(coe, x)]

def f(c, x):
    """
    主要爬山函式
    :param c: 函數的參數
    :param x: 變動的x
    :return: y
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i:  # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
    return sum

def restraint(x, r):
    """
    限制函式，用來減f(x)，當x的規則不合的時候，就不讓他進入if條件
    :param x: 變動的x
    :param r: 函數的限制條件，使用二維陣列存取，前面是參數，後面是限制數
    :return: 限制的逞罰，-100或是0(無逞罰)
    """
    sum = []
    if not len(r): # 沒有限制條件
        print("no restraction!")
        return 0

    for i in range(len(r)):
        sum.append(0)
        for j in range(len(r[i])-1):
            if len(x) > j: # 如果x比參數少就跳過，防止出錯
                if x[j] < 0:   # x為負數就逞罰
                    return -100
                sum[i] += r[i][j] * x[j]
        if sum[i] > r[i][len(r[i])-1]:  # 判斷基本條件
            return -100 
    return 0      

def ManAns(c, x):
    """
    用來算函數最大值
    :param c: 函數的參數
    :param x: 變動的x
    :return: 傳回函數的最大值
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i: # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
    return sum

def setWeights(c):
    """
    根據參數設定權重，參數越大，權重越重。
    :param c: 函數的參數
    :return: 權重列表
    """
    weight = [0] * len(c)  # 設定權重列表，根據參數做權重分配
    for i in range(len(coe)-1):  # 使用for迴圈分配權重
        for y in range(i ,len(coe)-1):  # 大於，目標權重-1，自己權重+1
            if coe[i] > coe[y]:
                weight[i] += 1
                weight[y] -= 1
            else:  # 小於，目標權重+1
                weight[y] += 1
    return weight

def findMaxWeightIndex(w):
    """
    尋找最大權重
    :param w: 權重列表
    :return: 最大權重值
    """
    for i in range(len(w)):
        if w[i] == max(w):
            return i

def ResetMaxWeight(w, num = -100):
    """
    用在當最大權重已經裝不下了，就把最大權重設定成一個極小值，換次大的權重開始往上加
    :param w: 權重列表
    :param num: 設定最大權重的值
    :return: 當還有可以繼續找的值就傳回True，反之Flase
    """
    max_index = findMaxWeightIndex(w)
    if w[max_index] != num:
        w[max_index] = num
        return True
    else:
        return False
    
startTime = datetime.now()
print(greedy(f, init_x))  # 打印最後結果    
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
```







