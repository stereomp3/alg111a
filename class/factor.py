def factorial(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r

if __name__ == '__main__':
    print('factorial(10)=', factorial(10))