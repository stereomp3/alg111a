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