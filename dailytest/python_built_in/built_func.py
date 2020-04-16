#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/15 10:55


if __name__ == '__main__':
    """abs() 取绝对值"""
    assert abs(-1) == 1

    """all(iterator) 迭代对象中 全部为True 才返回True"""
    assert all([0, '', None, False]) is False
    assert all([]) is True
    assert all(()) is True

    """any(iterator) 迭代对象中 有一个元素为True 就返回True"""
    assert any([0, '', None, False, True]) is True
    assert any([]) is False
    assert any(()) is False

    """basestring() 方法是 str 和 unicode 的超类（父类）"""
    assert isinstance('Hello', (str, unicode))
    assert isinstance('Hello', basestring)

    """bin()返回一个整数int或者长整数long int 的二进制表示"""
    assert bin(10) == '0b1010'
    assert isinstance(bin(20), basestring)

    """将给定参数转换为bool类型"""
    assert not bool()
    assert not bool(0)
    assert bool(1)
    assert issubclass(bool, int)  # bool 是int的子类

    """bytearray() 返回一个新的字节数组"""
    assert bytearray() == bytearray(b'')
    assert bytearray([1, 2, 3]) == bytearray(b'\x01\x02\x03')
    assert bytearray('hello', 'utf-8') == bytearray(b'hello')

    """callable() 检查函数是否是可调用的"""
    assert not callable(0)
    assert not callable('string')

    """chr() 返回整数对应的ASCII字符"""
    assert chr(0x61) == 'a'
    assert chr(97) == 'a'

    """classmethod 装饰类函数不需要实例化"""
    pass

    """cmp(x, y) 比较两个对象"""
    assert cmp(80, 100) == -1
    assert not cmp(80, 80)
    assert cmp(100, 80) == 1

    """compile() 将一个字符串编译为字节代码"""

    """complex() 创建一个复数"""

    """delattr() 删除属性"""
    # delattr(object, name)

    """dict() 创建一个字典"""
    assert dict(a='a', b='b', c='c') == {'a': 'a', 'b': 'b', 'c': 'c'}
    assert dict(zip(['a', 'b', 'c'], [1, 2, 3])) == {'a': 1, 'b': 2, 'c': 3}
    assert dict([('a', 1), ('b', 2), ('c', 3)]) == {'a': 1, 'b': 2, 'c': 3}

    """dir() """
    print dir()  # 获得当前模块的属性列表
    print dir([])  # 查看列表的方法

    """divmod() 返回商和余数的元组（a//b, a%b)"""
    assert divmod(7, 2) == (3, 1)
    assert divmod(1 + 2j, 1 + 0.5j) == ((1+0j), 1.5j)

    """enumerate() 将一个可遍历的数据对象 组合成 一个索引树"""
    # start: 下标起始位置
    assert list(enumerate(['Spring', 'Summer', 'Fall', 'Winter'], start=1)) == [(1, 'Spring'), (2, 'Summer'),
                                                                                (3, 'Fall'), (4, 'Winter')]

    """eval() 执行一个字符串表达式，并返回表达式的值"""
    n = 81
    assert eval('n + 1') == 82

    """execfile() 用来执行一个文件"""

    """file() 别名 open() 返回一个文件对象"""

    """filter(func, iterable) 返回符合过滤函数的新列表 """
    assert filter(lambda x: x % 2 == 1, range(1, 10)) == [1, 3, 5, 7, 9]

    """float() 将整数或字符串转换成浮点数"""
    assert float('123') == 123.0

    """format 格式化函数"""
    assert "{1} {0} {1}".format("hello", "world") == 'world hello world'
    assert "{:.2f}".format(3.1415926) == '3.14'

    """frozenset() 返回一个冻结（不能再添加和删除任何元素）的集合"""
    frozenset(range(10))

    """getattr() 返回一个对象的属性值"""
    getattr('obj', 'field', 'default')

    """globals() 以字典的形式返回当前位置的全部局部变量"""
    print globals()

    """hasattr() 判断对象是否包含对应的属性"""
    hasattr(object, 'field_name')

    """hash() 获取一个对象的哈希值"""
    assert -1267296259 == hash('hello')

    """help() 查看函数或模块用途的详细说明"""

    """hex() 将10进制整数转换成16进制，以字符串形式表示"""
    assert hex(255) == '0xff'
    assert issubclass(type(hex(255)), str)

    """id() 返回对象的唯一标识符， CPython 中id()函数用于获取对象的内存地址"""
    print id('hello')

    """input() raw_input() 获取控制台的输入"""
    # input('receive int:')
    # raw_input('all string:')  # 任何类型都以字符串接收

    """int() 将一个字符串或数字转换为整数"""
    assert int() == 0
    assert int('10', 16) == 16

    """isinstance() 判断一个对象是否是一个已知的类型，且支持继承关系，type()不考虑继承关系"""
    assert isinstance(2, int)
    assert isinstance(2, (str, int, list))

    """issubclass(class, classinfo) 判断参数class是否是classinfo的子类"""
    class A:
        pass
    class B(A):
        pass
    assert issubclass(B, A)

    """iter() 生成迭代器"""
    for i in iter(range(5)):
        print i

    """len() 返回对象（字符、列表、元组等）长度或项目个数"""
    assert len('hello') == 5

    """list(tuple) 将元组转换为列表"""
    assert isinstance(list((1, 2, 3)), list)

    """locals() 以字典类型返回当前位置的全部局部变量"""
    def func_c(args):
        field = 1
        print locals()
    func_c('arg')  # {'field': 1, 'args': 'arg'}

    """long() 将数字或字符串转换成一个长整型"""
    assert long('123') == 123L

    """map(function, iterable, ...) 根据提供的函数对指定序列做映射"""
    assert map(lambda x, y: x+y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [3, 7, 11, 15, 19]

    """max(x, y, z, ...) 返回给定参数的最大值"""
    assert max(-20, 0, 30) == 30
    assert max('1,2,3,4') == '4'

    """min(x, y, z, ...) 返回指定参数的最小值"""

    """memoryview(obj) 返回给定参数的内存查看对象"""
    view = memoryview('abcdef')
    assert view[-1] == 'f'
    print view[1:4]  # <memory at 0x02715760>
    assert view[1:3].tobytes() == 'bc'

    """next(iterator[, default]) 返回迭代器的下一个项目"""
    # 首先获得Iterator对象:
    it = iter([1, 2, 3, 4, 5])
    while True:
        try:
            # 获得下一个值:
            x = next(it)
            print(x)
        except StopIteration:
            # 没有下一个元素则会触发 StopIteration 异常
            break

    """oct() 将一个整数转换成8进制字符串"""
    assert '012' == oct(10)

    """open(name[, mode[, buffering]]) 打开一个文件，创建file对象"""

    """ord(char) 返回字符对应的ASCII数值"""
    assert ord('a') == 97

    """property() 在新式类中返回属性值"""
    class C(object):
        def __init__(self):
            self._x = None
        @property
        def x(self):
            """I'm the 'x' property."""
            return self._x
        @x.setter
        def x(self, value):
            self._x = value
        @x.deleter
        def x(self):
            del self._x

    """range(start, stop[, step]) 创建并返回一个整数列表"""

    """raw_input() 获取控制台的输入,返回结果都是字符串类型"""

    """reduce(function, iterable[, initializer]) 对参数序列中元素进行累积"""
    assert reduce(lambda a, b: a + b, range(0, 5)) == 10

    """reload(module) 重载之前载入的模块"""

    """repr(object) 将对象转化为供解释器读取的形式"""
    str_obj = 'hello'
    repr(str_obj)

    """reverse() 反转列表中的元素"""
    list_obj = [1, 2, 'a', 3.0, 0x55, 012]
    list_obj.reverse()
    assert [10, 85, 3.0, 'a', 2, 1] == list_obj

    """round(x[, n]) 返回浮点数x的四舍五入值（会受到计算机精度的影响）"""
    assert round(3.1415926, 4) == 3.1416

    """set([iterable]) 创建一个无序不重复元素集"""
    s1 = set('hello')
    s2 = set('world')
    assert s1 == {'h', 'e', 'l', 'o'}
    print s1 & s2  # 交集 set(['l', 'o'])
    print s1 | s2  # 并集 set(['e', 'd', 'h', 'l', 'o', 'r', 'w'])
    print s1 ^ s2  # 异或 set(['e', 'd', 'h', 'r', 'w'])
    print s1 - s2  # 差集 set(['h', 'e'])

    """setattr(object, name, value) 为对象设置属性值"""

    """slice(start, stop[, step]) 返回一个切片对象"""
    assert range(10)[slice(2, 6)] == [2, 3, 4, 5]

    """sorted(iterable, cmp=None, key=None, reverse=False) 对所有可迭代对象进行排序操作"""

    """staticmethod() 返回函数的静态方法"""

    """str() 将对象转化为适于人阅读的形式"""

    """"sum(iterable[, extra]) 求和计算"""
    assert sum((2, 3, 4), 1) == 10

    """super() 调用父类（超类）的一个方法"""
    class FooParent(object):
        def __init__(self):
            self.parent = 'I\'m the parent.'
            print ('Parent')
        def bar(self, message):
            print ("%s from Parent" % message)
    class FooChild(FooParent):
        def __init__(self):
            # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
            super(FooChild, self).__init__()
            print ('Child')
        def bar(self, message):
            super(FooChild, self).bar(message)
            print ('Child bar fuction')
            print (self.parent)

    """tuple(iterable) 将列表转换为元组"""
    assert tuple({'a': 1, 'b': 2}) == ('a', 'b')

    """type(name, bases, dict) 一个参数返回对象类型, 三个参数，返回新的类型对象。"""
    assert type('str') == str
    class X(object):
        a = 1
    obj = type('X', (object,), dict(a=1))
    print obj  # <class '__main__.X'>

    """unichr() 返回unicode的字符"""
    assert unichr(97) == u'a'

    """vars([object]) 返回对象object的属性和属性值的字典对象"""
    class Y(object):
        b = 2
    print(vars(Y))  # {'__dict__': <attribute '__dict__' of 'Y' objects>, '__module__': '__main__', 'b': 2, '__weakref__': <attribute '__weakref__' of 'Y' objects>, '__doc__': None}

    """xrange() 与range不同的是生成的不是一个数组，而是一个生成器"""
    xrange1 = xrange(3, 5)
    assert list(xrange1) == [3, 4]

    """zip([iterable, ...]) 将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表"""
    nums = ['flower', 'flow', 'flight']
    for i in zip(*nums):
        print(i)
    # ('f', 'f', 'f')
    # ('l', 'l', 'l')
    # ('o', 'o', 'i')
    # ('w', 'w', 'g')

    """__import__() 动态加载类和函数"""
    # 如果一个模块经常变化就可以使用 __import__() 来动态载入
