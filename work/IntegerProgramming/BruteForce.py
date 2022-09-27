from sqlalchemy import true


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
