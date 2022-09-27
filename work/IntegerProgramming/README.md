https://gitlab.com/cccnqu111/alg/-/blob/master/A2-QA/integerProgramming/README.md

解

```
4x1 + 7x2 + 3x3 + 8x4 + 5x5	≤ 211 
```



使用[暴力法](#暴力法)、[爬山演算法](#爬山演算法)、[貪婪法](#貪婪法)

## 暴力法

[BruteForce](BruteForce.py): 使用5個for迴圈解

```python
coe = [4, 7, 3, 8, 5]  
r = 211
BFN = r//min(coe)  # 取最小的可能下去做for迴圈次數  

def f(c, x):
    """
    function(f(x))
    :param C: 填入判斷函數，它會回傳函數的值 (f(x))
    :param x: 初始的位置，會慢慢的變動，直到f(x+dx)<f(x) && f(x-dx)<f(x)，就會跳出迴圈
    :param dx: 用來爬山的位移，函數內定好了
    :return: 答案列表
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
    for x1 in range(BFN):
        for x2 in range(BFN):
            for x3 in range(BFN):
                for x4 in range(BFN):
                    for x5 in range(BFN):
                        if IsEnd(f(coe, [x1, x2, x3, x4, x5]), r):
                            return [x1, x2, x3, x4, x5]

def IsEnd(sum, target):
    """
    判斷結果是不是等於最大值
    :param sum: 主要函數返回值(f(x))
    :param target: 目標值
    :return: 找到最終結果，返回True
    """
    if sum == target:
        return true

print(brute_force())  # 打印最後結果
```





## 爬山演算法

[hillClimbing01](hillClimbing01.py): 使用全部參數一同增長做處理，dx設定為1

最後結果如下: 

```sh
[8, 8, 8, 8, 7]
```

值等於 211

```python
coe = [4, 7, 3, 8, 5]  
init_x = [0, 0, 0, 0, 0]
r = 211

def hillClimbing(f, x, _dx=1):
    """
    主要爬山函式
    :param f: 填入判斷函數，它會回傳函數的值 (f(x))
    :param x: 初始的位置，會慢慢的變動，直到f(x+dx)<f(x) && f(x-dx)<f(x)，就會跳出迴圈
    :param dx: 用來爬山的位移，函數內定好了
    :return: max answer，值固定
    """
    peak = False
    while (not peak):
        for i in range(len(x)):
            tmpA = x.copy()  # 進行列表複製
            tmpD = x.copy()
            tmpA[i] += _dx
            tmpD[i] -= _dx
            if f(coe, tmpA)>f(coe, x) - restraint(coe, tmpA, r):
                x = tmpA
            elif f(coe, tmpD)>f(coe, x) - restraint(coe, tmpD, r):
                x = tmpD
            else:  # 最後對每個進行最後的運算
                peak = True  # 到頂了，下面會跳出迴圈，給定最大值
                break
    return x

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

def restraint(c, x, r):
    """
    限制函式，用來減f(x)，當x的規則不合的時候，就不讓他進入if條件
    :param c: 函數的參數
    :param x: 變動的x
    :param r: 函數的最大值 f(x) <= 211 ; r = 211
    :return: 限制的逞罰，-100或是0(無逞罰)
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i: # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
            if not 0 <= x[i] <= r/c[i]:  # 判斷基本條件 (整數、不大於限制條件)
                return -100
    if not sum <= 211:  # 判斷基本條件
        return -100
    else:
         return 0

print(hillClimbing(f, init_x))  # 打印最後結果

```



[hillClimbing02](hillClimbing02.py): 使用`random.randint(-_dx,_dx)`爬山，dx設定為1，對每一個x做加上random number的動作，如果找不到更大的值10000次，就代表目前的是最大值，答案是隨機的

```python
import random

coe = [4, 7, 3, 8, 5]  
init_x = [0, 0, 0, 0, 0]
r = 211
fail_times = 10000
def hillClimbing(f, x, _dx=1):
    """
    主要爬山函式
    :param f: 填入判斷函數，它會回傳函數的值 (f(x))
    :param x: 初始的位置，會慢慢的變動，直到f(x+dx)<f(x) && f(x-dx)<f(x)，就會跳出迴圈
    :param dx: 用來爬山的位移，使用random下去做位移
    :return:
    """
    fail_count = 0
    while (fail_count < fail_times):
        for i in range(len(x)):
            tmp = x.copy()  # 進行拷貝，利用新列表進行新舊判斷
            tmp[i] += random.randint(-_dx,_dx)  # 進行爬山位移
            if f(coe, tmp)>f(coe, x) - restraint(coe, tmp, r):
                x = tmp
                fail_count = 0
            else:  # 失敗
                fail_count += 1
    return x

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

def restraint(c, x, r):
    """
    限制函式，用來減f(x)，當x的規則不合的時候，就不讓他進入if條件
    :param c: 函數的參數
    :param x: 變動的x
    :param r: 函數的最大值 f(x) <= 211 ; r = 211
    :return: 限制的逞罰，-100或是0(無逞罰)
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i: # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
            if not 0 <= x[i] <= r/c[i]:  # 判斷基本條件 (整數、不大於限制條件)
                return -100
    if not sum <= 211:  # 判斷基本條件
        return -100
    else:
         return 0

print(hillClimbing(f, init_x))  # 打印最後結果
```







## 貪婪法

貪婪法: 係數最大的開始下手，使用一個列表紀錄權重，係數越大，權重越重，從權重大的開始往上加

最後結果如下: 

```
[0, 0, 1, 26, 0]
```

值等於 211

```python
coe = [4, 7, 3, 8, 5]  
init_x = [0, 0, 0, 0, 0]
r = 211

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
        
        if f(coe, tmp)>f(coe, x) - restraint(coe, tmp, r):
            x = tmp
        else:  
            if not ResetMaxWeight(weight):  
                break
            max_index = findMaxWeightIndex(weight)  # 重新設定權重
                
    return x

def f(c, x):
    """
    主要函式
    :param c: 函數的參數
    :param x: 變動的x
    :return: y
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i:  # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
    return sum

def restraint(c, x, r):
    """
    限制函式，用來減f(x)，當x的規則不合的時候，就不讓他進入if條件
    :param c: 函數的參數
    :param x: 變動的x
    :param r: 函數的最大值 f(x) <= 211 ; r = 211
    :return: 限制的逞罰，-100或是0(無逞罰)
    """
    sum = 0
    for i in range(len(c)):
        if len(x) > i: # 如果x比參數少就跳過，防止出錯
            sum += c[i] * x[i]
            if not 0 <= x[i] <= r/c[i]:  # 判斷基本條件 (整數、不大於限制條件)
                return -100
    if not sum <= 211:  # 判斷基本條件
        return -100
    else:
         return 0

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
   
print(greedy(f, init_x))  # 打印最後結果    
```







