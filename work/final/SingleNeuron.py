import math


class Unit:
    """
        Units we also need 3 gates: +, * and sig (sigmoid).
    """

    def __init__(self, value, grad):
        self.value = value  # value computed in the forward pass
        self.grad = grad  # derivative of circuit output


class multiplyGate:  # *
    def __init__(self):
        self.u0 = None  # Unit(0, 0)
        self.u1 = None
        self.utop = None

    def forward(self, u0, u1):  # 初始化
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(u0.value * u1.value, 0)
        return self.utop

    def backward(self):  # 使用Analytic Gradient，求得u0的偏微分和u1的偏微分
        self.u0.grad += self.u1.value * self.utop.grad
        self.u1.grad += self.u0.value * self.utop.grad


class addGate:  # +
    def __init__(self):
        self.u0 = None  # Unit(0, 0)
        self.u1 = None
        self.utop = None

    def forward(self, u0, u1):  # 初始化
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(u0.value + u1.value, 0)
        return self.utop

    def backward(self):  # 使用Analytic Gradient，求得u0的偏微分和u1的偏微分
        self.u0.grad += 1 * self.utop.grad
        self.u1.grad += 1 * self.utop.grad


class sigmoidGate:  # sigmoid
    def __init__(self):
        self.u0 = None  # Unit(0, 0)
        self.utop = None

    def forward(self, u0):  # 初始化
        self.u0 = u0
        self.utop = Unit(sigmoidGate.sig(self, self.u0.value), 0)
        return self.utop

    def backward(self):  # 使用Analytic Gradient，求得u0的偏微分和u1的偏微分
        s = sigmoidGate.sig(self, self.u0.value)
        self.u0.grad += (s * (1 - s)) * self.utop.grad

    def sig(self, x):
        return 1 / (1 + math.exp(-x))


a = Unit(1, 0)
b = Unit(2, 0)
c = Unit(-3, 0)
x = Unit(-1, 0)
y = Unit(3, 0)

mulg0 = multiplyGate()
mulg1 = multiplyGate()
addg0 = addGate()
addg1 = addGate()
sg0 = sigmoidGate()
output = None


def forwardNeuron():
    ax = mulg0.forward(a, x)  # a*x = -1
    by = mulg1.forward(b, y)  # b*y = 6
    axpby = addg0.forward(ax, by)  # a*x + b*y = 5
    axpbypc = addg1.forward(axpby, c)  # a*x + b*y + c = 2
    global output
    output = sg0.forward(axpbypc)  # sig(a*x + b*y + c)
    # print(output.value)


forwardNeuron()  # s.value = 0.8807970779778823
output.grad = 1.0
sg0.backward()
addg1.backward()
addg0.backward()
mulg1.backward()
mulg0.backward()

step_size = 0.01
a.value += step_size * a.grad  # -0.10499358540350662
b.value += step_size * b.grad  # 0.31498075621051985
c.value += step_size * c.grad  # 0.10499358540350662
x.value += step_size * x.grad  # 0.10499358540350662
y.value += step_size * y.grad  # 0.20998717080701323

forwardNeuron()  # s.value = 0.8825501816218984




# def forwardCircuitFast(a, b, c, x, y):
#     return 1/(1 + math.exp(-(a*x + b*y + c)))
# # numerical gradient check
# a = 1; b = 2; c = -3; x = -1; y = 3
# h = 0.0001
# a_grad = (forwardCircuitFast(a+h,b,c,x,y) - forwardCircuitFast(a,b,c,x,y)) / h
# b_grad = (forwardCircuitFast(a,b+h,c,x,y) - forwardCircuitFast(a,b,c,x,y)) / h
# c_grad = (forwardCircuitFast(a,b,c+h,x,y) - forwardCircuitFast(a,b,c,x,y)) / h
# d_grad = (forwardCircuitFast(a,b,c,x+h,y) - forwardCircuitFast(a,b,c,x,y)) / h
# e_grad = (forwardCircuitFast(a,b,c,x,y+h) - forwardCircuitFast(a,b,c,x,y)) / h
# print(a_grad)
# print(b_grad)
# print(c_grad)
# print(d_grad)
# print(e_grad)