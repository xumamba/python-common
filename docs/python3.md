# Python3

## Python Base
  - ```... ```
  - 空值:None
  - 动态语言——变量本身类型不固定
  - 可以把变量a赋值给变量b，这个操作实际上是把变量b指向变量a所指向的数据
  - 常量：用全部大写的变量名表示
  - 除法
    
    - / 结果都是浮点数：10 / 3 == 3.3333333333    9 / 3 == 3.0 
    - // 地板除 结果都是整数（取整数部分）： 10 // 3 == 3
    - % 取余数： 10 % 3 == 1   
  - Python的整数没有大小限制
  - Python的浮点数也没有大小限制,但是超出一定范围就直接表示为 inf (无限大)。
  - ASCII（1字节）----Unicode（2字节）----UTF-8（英文1，汉字3字节）
  - ord('A')   chr(65)
  - 字符串
    - 
    - 在Python 3版本中,字符串是以Unicode编码的,也就是说,Python的字符串支持多语言
    - Python对 bytes 类型的数据用带 b 前缀的单引号或双引号表示 x = b'ABC'
    - Unicode表示的 str 通过 encode() 方法可以编码为指定的 bytes
    - b'ABC'.decode('utf-8') 解码
    - len() 求字符、字节数
    - 解释器读取源代码时,为了让它按UTF-8编码读取,在文件开头写上这两行:
    ```python
        1. #!/usr/bin/env python3
        2. # -*- coding: utf-8 -*-
      ```
    - 字符串替换 str.replace('a','A')
  - list
    - 
    - 有序列表  names = ['aa','bb','cc']
    - 取倒数第一个    lt[-1]
    - 指定位置插入元素 lt.insert(1,'test')
    - 删除末尾的元素   lt.pop()  
    - 删除指定位置的元素 lt.pop(index)
    - 元素排序 lt.sort()
    - list里面的元素的类型也可以不同
  - tuple
    - 
    - 有序列表，一旦初始化就不能修改 name = ('aa','bb','cc')
    - 只有一个元素，注意逗号（1，）
    - “可变的”tuple ([list])
  - 条件判断
    -
    - elif <条件判断>: 
    - if x : 只要 x 是非零数值、非空字符串、非空list等,就判断为 True ,否则为 False 
    - input() 返回的数据类型是 str  int(str)
  - 循环
    - 
    - for name in names:
    - range() 生成一个整数序列  
    ```python
        1. >>> list(range(5))
        2. [0, 1, 2, 3, 4]

        sum = 0
        for x in range(101): 
            sum = sum + x
        print sum
     ```
    - while <条件判断>:
    - raw_input()读取的内容永远以字符串的形式返回
    ```python
    birth = int(raw_input('birth: '))
    ```
  - dict
    - 
    - d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    - d['Adam'] = 67
    - in 判断key是否存在 'Thomas' in d
    - d.get('Thomas', -1)  // 不存在时返回自己指定的-1
    - 删除元素 pop()
    - dict是用空间来换取时间的一种方法
  - set
    - 
    - 要创建一个set,需要提供一个list作为输入集合: s = set([1, 2, 3])
    - 添加 add(key)
    - 删除 remove(key)
    - set之间 交（&） 并（|）集 
    
  - 对于不变对象来说,调用对象自身的任意方法,也不会改变该对象自身的内容。相反,这些方法
会创建新的对象并返回,这样,就保证了不可变对象本身永远是不可变的。
  - 函数
    -
    - 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋值给一个变量，相当于给这个函数起了一个“别名”
    - pass
    - isinstance()
    ```python
        def my_abs(x):
            if not isinstance(x, (int, float)):
                raise TypeError('bad operand type')
            if x >= 0:
                return x
            else:
                return -x
    ```
    - Python返回值是一个tuple!但是,在语法上,返回一个tuple可以省略括号,而多个变量可以同时接收一个tuple,按位置赋给对应的值,所以,Python的函数返回多值其实就是返回一个tuple,但写起来更方便。
    - 函数执行完毕也没有 return 语句时,自动 return None
    - 默认参数必须指向不变对象!
    - 可变参数 *，函数内部按tuple处理
    - 在list或tuple前面加一个 * 号,把list或tuple的元素变成可变参数传进去
    - 关键字参数允许你传入0个或任意个含参数名的参数,这些关键字参数在函数内部自动组装为一个dict
    - 和关键字参数 *kw 不同,命名关键字参数需要一个特殊分隔符*
    ```python
        def f1(a, b, c=0, *args, **kw):
            print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
        def f2(a, b, c=0, *, d, **kw):
            print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    ```
    - 在Python中定义函数,可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数,这5种参数都可以组合使用,除了可变参数无法和命名关键字参数混合。但是请注意,参数定义的顺序必须是:必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
    ```python
        def person(name, age, *, city='XiaMen', job):
            print(name, age, city, job)
    ```
    - 栈溢出
        
        - 尾递归优化
        - 尾递归是指,在函数返回的时候,调用自身本身,并且,return语句不能包含表达式。这样,编译器或者解释器就可以把尾递归做优化,使递归本身无论调用多少次,都只占用一个栈帧,不会出现栈溢出的情况。
  - 高级特性
    - 
    - 切片
      - 
      - L[-2:-1]
      - L[:10:2]   前10个元素，每两个取一个 [0,2,4,6,8]
      - L[::5]     所有数，每5个取一个
      - L[:]   复制list
      - tuple切片操作结果仍是tuple
      - 字符串也可以做切片操作，每个元素就是一个字符，结果仍是字符串
    - 迭代
      - 
      - for ... in
      - for key in dict:  for value in d.values():   for k,v in d.items():
      - 判断是否可迭代
      ```python
        from collections import Iterable
        isinstance('abc', Iterable) # str是否可迭代
        True
        isinstance([1,2,3], Iterable) # list是否可迭代
        True
        isinstance(123, Iterable) # 整数是否可迭代
        False
        for i, value in enumerate(['A', 'B', 'C']):
          print(i, value)
        0 A
        1 B
        2 C
        ```
    - 列表生成式
      - 
      - [x * x for x in range(1, 11)] ---> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
      - [x * x for x in range(1, 11) if x % 2 == 0] ---> [4, 16, 36, 64, 100]
      - [m + n for m in 'ABC' for n in 'XYZ'] ---> ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    - 生成器
      - 
      - 一边循环一边计算的机制,称为生成器:generator
      - 创建generator:
        
        - 把一个列表生成式的 [] 改成 () 
        - ```python
            g = (x * x for x in range(10))
            next(g)
          
            g = (x * x for x in range(10))
            for n in g:
              print(n)
          ```
         - 如果一个函数定义中包含 yield 关键字,那么这个函数就不再是一个普通函数,而是一个generator
         - ```python
             def fib(max):
               n, a, b = 0, 0, 1
               while n < max:
                  yield b
                  a, b = b, a + b
                  n = n + 1
               return 'done'
           
           
             for n in fib(6):
               print(n)
           ```
          - generator的函数,在每次调用 next() 的时候执行,遇到 yield 语句返回,再次执行时从上次返回的 yield 语句处继续执行。
          - 如果想要拿到返回值,必须捕获 StopIteration 错误,返回值包含在 StopIteration 的 value 中
          - ```python
              g = fib(6)
              while True:
                 try:
                   x = next(g)
                   print('g:', x)
                 except StopIteration as e:
                   print('Generator return value:', e.value)
                   break
            ```
    - 迭代器
      -
      - list 、 dict 、 str 等数据类型不是 Iterator
      - list 、 dict 、 str 等 Iterable 变成 Iterator 使用 iter() 函数 isinstance(iter([]), Iterator)  --- > true
      - Iterator 对象表示的是一个数据流,Iterator 的计算是惰性的,只有在需要返回下一个数据时它才会计算
  - 函数式编程
    - 
    - [MapReduce: Simplified Data Processing on Large Clusters](http://research.google.com/archive/mapreduce.html)
    - map() 函数接收两个参数,一个是函数,一个是 Iterable,map 将传入的函数依次作用到序列的每个元素,并把结果作为新的 Iterator 返回
    - ```python
       list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
       ['1', '2', '3', '4', '5', '6', '7', '8', '9']
      ```
    - reduce() 把一个函数作用在一个序列 [x1, x2, x3, ...] 上,这个函数必须接收两个参数, reduce 把结果 继续和序列的下一个元素做累积计算
    - reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    - filter()也接收一个函数和一个序列。和 map() 不同的是, filter() 把传入的函数依次作用于每个元素,然后根据返回值是 True 还是 False 决定保留还是丢弃该元素。
    - filter返回的是一个Iterator list()
    - sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
    - 返回函数
      - 
      - 闭包：返回函数不要引用任何循环变量,或者后续会发生变化的变量。
      - 关键字 lambda 表示匿名函数,冒号前面的 x 表示函数参数。
      - ```python
        lambda x: x * x
        def f(x):
           return x * x
        ```
      - 匿名函数有个限制,就是只能有一个表达式,不用写 return ,返回值就是该表达式的结果。
      - 装饰器：
         
        - 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator)
        - decorator就是一个返回函数的高阶函数。
        - ```python
          def log(func):
              def wrapper(*args, **kw):
                  print('call %s():' % func.__name__)
                  return func(*args, **kw)
              return wrapper
          
          
          import functools
          
          def log(text):
            def decorator(func):
              @functools.wraps(func)
              def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
              return wrapper
            return decorator
          ```
        - @decorator
        - 偏函数：int2 = functools.partial(int, base=2)
        - 当函数的参数个数太多,需要简化时,使用 functools.partial 可以创建一个新的函数,这个新函数可以固定住原函数的部分参数,从而在调用时更简单。
  - 模块
    - 
    - 在Python中,一个.py文件就称之为一个模块(Module)
    - [Python的所有内置函数](https://docs.python.org/3/library/functions.html)
    - 每一个包目录下面都会有一个 init.py 的文件,这个文件是必须存在的,否则,Python就把这个目录当成普通目录,而不是一个包。
    - init.py 可以是空文件,也可以有Python代码,因为 init.py 本身就是一个模块,而它的模块名就是包名
    - 任何模块代码的第一个字符串都被视为模块的文档注释
    - sys 模块有一个argv 变量,用list存储了命令行的所有参数
    - ```python
        if __name__ == '__main__':
          test()
      ```
    - 当我们在命令行运行 hello 模块文件时,Python解释器把一个特殊变量 name 置为 main ,而如果在其他地方导入该 hello 模块时, if 判断将失败,因此,这种 if 测试可以让一个模块通过命令行运行时执行一些额外的代码,最常见的就是运行测试。
    - 作用域  _private
    - 第三方库都会在Python官方的[pypi.python.org](https://pypi.org/)网站注册
    - 添加自己的搜索目录：
      
      - 直接修改 sys.path ,添加要搜索的目录 sys.path.append('‘)
      - 设置环境变量 PYTHONPATH ,该环境变量的内容会被自动添加到模块搜索路径中
  - Object Oriented Programming
    -
    - 如果要让内部属性不被外部访问,可以把属性的名称前加上两个下划线  python解释器  bart._Student__name
    - Python中,变量名以双下划线开头,并且以双下划线结尾的,是特殊变量,特殊变量是可以直接访问的,不是private变量
    - 对扩展开放，对修改封闭。
    - type(obj)   import types
    - 获取一个对象的所有属性和方法：dir()函数，它返回一个包含字符串的list
    - getattr() 、 setattr() 以及 hasattr()
    - 实例属性 和 类属性，命名注意
    - Student.set_score = MethodType(set_score, Student)  后期给class绑定方法
    - __slots__=('name','age') #用tuple定义允许绑定的属性名称
    - slots 定义的属性仅对当前类实例起作用,对继承的子类是不起作用的
    - Python内置的 @property 装饰器就是负责把一个方法变成属性调用的
    - MixIn 多重继承
    - ForkingMixIn 多进程 ThreadingMixIn 多线程  CoroutineMixIn
    - 自定义的类可以表现得和Python自带的list、tuple、dict没什么区别
    - call() 方法,可以直接对实例进行调用
    - callable() 函数,可以判断一个对象是否是“可调用”对象
    - from enum import Enum
    - Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'))
    - metaclass
  - 错误、调试和测试
    -
    - Python的错误其实也是class，所有的错误类型都继承自BaseException
    - raise 语句如果不带参数,就会把当前错误原样抛出。
    - assert n != 0, 'n is zero!'
    - 启动Python解释器时可以用 -O 参数来关闭 assert
    - 