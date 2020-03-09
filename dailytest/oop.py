
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object(name:%s)' % self.name

    __repr__ = __str__

    # 实现for ... in ... 可迭代
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration
        return self.a

    # 表现得如list
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a


if __name__ == '__main__':
    stu = Student('name')
    print(stu)
    print(stu[5])
