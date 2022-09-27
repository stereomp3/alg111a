coe = [4, 7, 3, 8, 5]  
init_x = [0, 0, 0, 0, 0]
r = 211

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
