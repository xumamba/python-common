import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    result = unittest.fact(5)
    print(result)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)


print(fact(5))
print(fact2(5))


def move(n, a, b, c):
    if n == 1:
        print('move:', a, '--->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


move(5, 'A', 'B', 'C')

