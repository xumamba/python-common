from functools import reduce


def normalize(name):
    new = name[0].upper()+name[1:]
    return new



L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))


print(L2)
# ['Adam', 'LISA', 'BarT']


def quadrature(x, y):
    return x * y


def prod(li):
    return reduce(quadrature, li)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# 3 * 5 * 7 * 9 = 945

