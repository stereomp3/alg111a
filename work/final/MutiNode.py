import random


def forwardMultiplyGate(a, b):
    return a * b


def forwardAddGate(a, b):
    return a + b


def forwardCircuit(x, y, z):
    q = forwardAddGate(x, y)
    f = forwardMultiplyGate(q, z)
    return f


x = -2
y = 5
z = -4
# forwardCircuit(x, y, z)  # -12

# Analytic Gradient
q = forwardAddGate(x, y)  # 3
f = forwardMultiplyGate(q, z)  # -12

derivative_f_wrt_z = q  # 3
derivative_f_wrt_q = z  # -4

derivative_q_wrt_x = 1.0
derivative_q_wrt_y = 1.0

# chain rule
derivative_f_wrt_x = derivative_q_wrt_x * derivative_f_wrt_q  # 4
derivative_f_wrt_y = derivative_q_wrt_y * derivative_f_wrt_q  # -4

# final gradient [-4, -4, 3]  # 對每個輸入做偏微分的向量
gradient_f_wrt_xyz = [derivative_f_wrt_x, derivative_f_wrt_y, derivative_f_wrt_z]

step_size = 0.01
x = x + step_size * derivative_f_wrt_x  # -2.04
y = y + step_size * derivative_f_wrt_y  # 4.96
z = z + step_size * derivative_f_wrt_z  # -3.97

q = forwardAddGate(x, y)  # 2.92
f = forwardMultiplyGate(q, z)  # -11.5924
