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