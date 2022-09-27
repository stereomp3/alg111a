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
            max_index = findMaxWeightIndex(weight) 
                
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

def setWeights(c):
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
    for i in range(len(w)):
        if w[i] == max(w):
            return i

def ResetMaxWeight(w, num = -100):
    max_index = findMaxWeightIndex(w)
    if w[max_index] != num:
        w[max_index] = num
        return True
    else:
        return False
    



print(greedy(f, init_x))  # 打印最後結果    
