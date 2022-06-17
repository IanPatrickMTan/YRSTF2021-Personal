import numpy as np

def test(x):
    return 3 * x ** 2

def altTest1(x):
    x = x / 2
    return x ** 3 + 3 * x ** 2 + x

def cost(x):
    return (5 - test(x)) ** 2

def nadm(func, x, m, dx = 0.01, b = 0.9, r = 0.01):
    g = (func(x + dx) - func(x)) / dx
    nm = b * m + r * g
    return x - (b * nm + r * g), nm

def g(func, x, dx = 0.01, r = 0.01):
    if type(x) == list:
        g = (func(x[0] + dx) - func(x[0])) / dx
        return [x[0] - g * r]
    else:
        g = (func(x + dx) - func(x)) / dx
        return x - g * r

def mm(func, a, dx = 0.01, b = 0.9, r = 0.01):
    x, m = a
    g = (func(x + dx) - func(x)) / dx
    m = b * m + r * g
    return x - m, m

def nm(func, a, dx = 0.01, b = 0.9, r = 0.01):
    x, m = a
    x = x - b * m
    g = (func(x + dx) - func(x)) / dx
    m = b * m + r * g
    return x - m, m

def p1(func, a, dx = 0.01, b = 0.9, r = 0.01):
    x, v = a
    #x = x - b * v
    g = (func(x + dx) - func(x)) / dx
    v = b * v + r * g
    return x - v * np.tanh(g), v

def p2(func, a, dx = 0.01, b = 0.9, r = 0.01):
    x, v = a
    #x = x - b * v
    g = (func(x + dx) - func(x)) / dx
    v = b * v + r * g
    return x - v * (g / abs(g)), v

def p3(func, a, dx = 0.01, b = 0.9, r = 0.01):
    x, v = a
    x = x - b * v
    g = (func(x + dx) - func(x)) / dx
    v = b * v + r * g
    return x - v * np.tanh(g), v

def p4(func, a, dx = 0.01, b = 0.9, r = 0.01):
    x, v = a
    #x = x - b * v
    g = (func(x + dx) - func(x)) / dx
    v = b * v + r * g
    return x - v * np.tanh(g), v

def kor(func, a, dx = 0.01, b = 0.9, r = 0.01):
    x, v, be = a
    g = (func(x + dx) - func(x)) / dx
    nv = be * v + r * g
    be = b + (1 - b) * np.tanh(nv - v)
    return x - (b * w + r * g), v, be


def graph(x, op, func, a):
    o = []
    for y in range(x - 1):
        o.append(f'{test(a[0])}')
        a = op(func, a)
    o.append(f'{test(a[0])}')
    f = open('test results', 'w')
    f.write('\n'.join(o))
    f.close()

a = [23, 0]
print('Results have been saved!')
