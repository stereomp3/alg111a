import random


def forwardMultiplyGate(x, y):
    return x * y


x = -2
y = 3

# # Random Local Search
# tweak_amount = 0.01  # 調整數
# best_out = -10000000000000  # -Infinity
# print(forwardMultiplyGate(x, y))
# best_x = x; best_y = y
# for k in range(100):
#     x_try = x + tweak_amount * (random.random() * 2 - 1)  # 調整一點x
#     y_try = y + tweak_amount * (random.random() * 2 - 1)  # 調整一點y
#     out = forwardMultiplyGate(x_try, y_try)
#     if out > best_out:
#         best_out = out
#         best_x = x_try; best_y = y_try
# print(best_out)  # -5.95

# # Numerical Gradient
# out = forwardMultiplyGate(x, y)  # 6
# h = 0.0001
# xph = x + h
# out2 = forwardMultiplyGate(xph, y)  # -5.9997
# x_derivative = (out2 - out) / h  # 對 x 做偏微分  3.00000000000189
#
# yph = y + h
# out3 = forwardMultiplyGate(x, yph)  # -6.0002
# y_derivative = (out3 - out) / h  # 對 y 做偏微分  -2.0000000000042206
#
# # gradient is just made up of the derivatives of all the inputs concatenated in a vector
# step_size = 0.01
# x = x + step_size * x_derivative  # 乘上梯度方向
# y = y + step_size * y_derivative  # 乘上梯度方向
# out_new = forwardMultiplyGate(x, y)  # -5.87059999999986
# # 梯度法(-5.87)比起前面的random效果好的多

# # Analytic Gradient
# # 上一個做法還是有點不太好，因為要調整每個獨立的輸入，對於今天有好幾百萬甚至上億節點的運算，會花費很多效能
# out = forwardMultiplyGate(x,y)
# x_gradient = y
# y_gradient = x
#
# step_size = 0.01
# x += step_size * x_gradient
# y += step_size * y_gradient
# out_new = forwardMultiplyGate(x, y)
# print(out_new)
