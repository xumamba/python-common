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