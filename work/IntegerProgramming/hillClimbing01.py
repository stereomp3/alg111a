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