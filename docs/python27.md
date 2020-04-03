# Python2.7

## Python基础

  - 空值:None
  - 动态语言——变量本身类型不固定
  - 可以把变量a赋值给变量b，这个操作实际上是把变量b指向变量a所指向的数据
  - 常量：用全部大写的变量名表示
  - 10 % 3 == 1   
  - ASCII----Unicode----UTF-8
  - ord('A')   chr(65)
  - Unicode表示的字符串用u‘...'表示，u‘中文’  u‘中' u'\u4e2d'
    
    - u'中文'.encode('utf-8') 
    - len(u'ABC') ---> 3
    - len('ABC') ---> 3
    - len(u'中文') ---> 2
    - len('\xe4\xb8\xad\xe6\x96\x87') ---> 6
    - 'abc'.decode('utf-8') ---> u'abc'
    - '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') ---> u'\u4e2d\u6587'
    - 
    ```python
       #!/usr/bin/env python   
       # -*- coding: utf-8 -*-
     ```
  - bool 
    - bool值 可以用 and, or, not 计算
  - 除法运算
    - 10/3 == 3
    - 10.0/3 == 3.33333333335
    - 10%3 == 1
  - 字符串格式化
    - 'Hi, %s, you have $%d.' % ('Michael', 1000000)
    - | %d | 整数 || %f | 浮点数 || %s | 字符串 || %x | 十六进制整数 |
    - '%2d-%02d' % (3, 1) --->  ' 3-01'
    - '%.2f' % 3.1415926  --->  '3.14'
  - list
  
    - 有序列表 
    - 取倒数第一个    lt[-1]
    - 指定位置插入元素 lt.insert(1,'test')
    - 删除末尾的元素   lt.pop()  
    - 删除指定位置的元素 lt.pop(index)
    - list里面的元素的类型也可以不同
  - tuple
    
    - 有序列表，一旦初始化就不能修改
    - 只有一个元素，注意逗号（1，）
    - “可变的”tuple ([list])
  - 条件判断
  
    - elif <条件判断>: 
    - if x : 只要 x 是非零数值、非空字符串、非空list等,就判断为 True ,否则为 False 
  - 循环
    
    - for name in names:
    - range() 生成一个整数序列  
    ```python
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
  
    - d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    - d['Adam'] = 67
    - in 判断key是否存在 'Thomas' in d
    - d.get('Thomas', -1)  // 不存在时返回自己指定的-1
    - 删除元素 pop()
    - dict是用空间来换取时间的一种方法
  - set
  
    - 要创建一个set,需要提供一个list作为输入集合: s = set([1, 2, 3])
    - 添加 add(key)
    - 删除 remove(key)
    - set之间 交（&） 并（|）集  差（^)集
    - 对于不变对象来说,调用对象自身的任意方法,也不会改变该对象自身的内容。相反,这些方法
会创建新的对象并返回,这样,就保证了不可变对象本身永远是不可变的。
- 函数
    - 
    - 函数名其实就是指向一个函数对象的引用,完全可以把函数名赋给一个变量,相当于给这个函数起了一个“别名”
    - 返回一个tuple可以省略括号,而多个变量可以同时接收一个tuple,按位置赋给对应的值
    - 默认参数必须指向不变对象（python函数在定义的时候，默认参数的值就被计算出来了）
    - 可变参数，函数内部接收到的是一个tuple
    - 在list或tuple前面加一个 * 号,把list或tuple的元素变成可变参数传进去
    - 关键字参数在函数内部是一个字典
    - 在dict前面加一个 ** 号,直接作为关键字传入整个字典
    - 对于任意函数,都可以通过类似 func(*args, **kw) 的形式调用它,无论它的参数是如何定义的
    - 尾递归是指,在函数返回的时候,调用自身本身,并且,return语句不能包含表达式（循环）
- 高级特性
    -
    - 切片，字符串也可以
    - 迭代
        - dict迭代的是key。如果要迭代value,可以用 for value in d.itervalues()
        - 同时迭代key和value,可以用 for k, v in d.iteritems()
        - 字符串也是可迭代对象
        - 通过collections模块的Iterable类型判断是否是可迭代对象：isinstance('abc', Iterable)
        - for i, value in enumerate(['A', 'B', 'C']):同时迭代索引值和本身
    - 列表生成器
        - [x * x for x in range(1, 11) if x % 2 == 0] ---> [4, 16, 36, 64, 100]
        - [m + n for m in 'ABC' for n in 'XYZ'] ---> ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
        - [d for d in os.listdir('.')]
        - [s.lower() for s in L]
    - 生成器Generator
        - 一边循环一边计算
        - 把一个列表生成式的 [] 改成() ,就创建了一个generator
        - generator.next()
        - generator也是一个可迭代对象
        - yield关键字 创建生成器，函数执行遇到yield返回，下次next(),从yield开始执行
 - 函数式编程
    -
    - 闭包
        - 返回闭包时牢记的一点就是:返回函数不要引用任何循环变量,或者后续会发生变化的变量。
    - 匿名函数
        - lambda  
        - f = lambda x: x * x
    - 装饰器
        - functools.warps(func)
    - 偏函数
        - functools.partial
        - functools.partial 的作用就是,把一个函数的某些参数给固定住(也就是设置默认值),返回一个新的函数,调用这个新函数会更简单。
 - 模块
    -
    - 任何模块代码的第一个字符串都被视为模块的文档注释
    - sys.argv 用list存储了命令行的所有参数
    - ```python
        try:
          import cStringIO as StringIO
        except ImportError: # 导入失败会捕获到ImportError
          import StringIO
      ```
    - 由于Python是动态语言,函数签名一致接口就一样,因此,无论导入哪个模块后续代码都能正常工作。
    - 作用域
        - _
        - from __future__
 - 面向对象编程
    -
    - __私有变量:解释器把它改成了 _ClassName__私有变量
    - __特殊变量__:可以被外部访问，非private
    - 开闭原则：
        - 对扩展开放
        - 对修改封闭
    - 判断对象类型：type()
    - 所有类型本身的类型就是TypeType
    - dir(obj) 获取一个对象的所有属性和方法 字符串list
    - getattr() 、 setattr() 以及 hasattr()
 - 面向对象高级编程
    - 
    - 可以给实例或者类绑定方法
    - __slots__=('name','age') #用tuple定义允许绑定的属性名称
    - slots 定义的属性仅对当前类起作用,对继承的子类是不起作用的
    - 类允许定义的属性就是自身的 slots 加上父类的 slots
    - @property装饰器负责把一个方法变成属性调用
    - ```python
        class Student(object):
              @property
              def score(mcs):
              return mcs._score
      
              @score.setter
              def score(mcs, value):
                  if not isinstance(value, int):
                      raise ValueError('score must be an integer!')
                  if value < 0 or value > 100:
                      raise ValueError('score must between 0 ~ 100!')
                  mcs._score = value
      ```
    - 只定义getter方法,不定义setter方法就是一个只读属性:
    - Mixin多重继承：
        - class MyTCPServer(TCPServer, ForkingMixin):
    - 定制类
    - 动态语言和静态语言最大的不同,就是函数和类的定义,不是编译时定义的,而是运行时动态创建的
    - 除了使用 type() 动态创建类以外,要控制类的创建行为,还可以使用metaclass。
- 错误、调试、测试
    -
    - 所有错误类型都继承自BaseException
    - 错误是class,捕获一个错误就是捕获到该class的一个实例
    - raise 抛异常
    - assert 断言失败会抛出AssertionError
    - -O 关闭断言：$ python -O err.py，assert 相当于pass
    - logging:debug , info , warning , error
        ```python
        import logging
        logging.basicConfig(level=logging.INFO)
        ```
    - 单元测试：class TestXXX(unittest.TestCase)
        - mcs.assertEquals()
        - with mcs.assertRaises(KeyError)
        - with mcs.assertRaises(AttributeError)
        - 在命令行通过参数 -m unittest 直接运行单元测试($ python -m unittest mydict_test)
        - setUp() 和 tearDown()分别在每调用一个测试方法的前后分别被执行
    - 文档测试
        - doctest不但可以用来测试,还可以直接作为示例代码。通过某些文档生成工具,就可以自动把包含doctest的注释提取出来   
- IO编程
    -
    - 操作系统同一时间能打开的文件数量也是有限的
    - ```python
       with open('/path/to/file', 'r') as f:
          print f.read()
      ```
    - 操作文件和目录
    - 序列化
        - (pickling,unpickling)只能用于python
            - cPickle 和 pickle
            - pickle.dumps() 方法把任意对象序列化成一个str,pickle.loads()反序列化
            - pickle.dump() 直接把对象序列化后写入一个file-like Object（pickle.load()反序列化）:
             ```python
             f = open('dump.txt', 'wb')
             pickle.dump(d, f)
             f.close()
             ```
        - JSON
            - import json
            - str = json.dumps(obj)
            - json.loads(json_str)
            - 序列化得到的所有字符串对象默认都是 unicode 而不是 str
            - json.dumps(s, default=lambda obj: obj.__dict__)
            - 通常 class 的实例都有一个 dict 属性,它就是一个 dict ,用来存储实例变量。也有少数例外,比如定义了 slots 的class
            - json.loads(json_str, object_hook=dict2student)
- 进程和线程
    -
    - multiprocessing
    - 进程间通信
      - Queue、Pipes
      - process.start process.join  process.terminate
      - 父进程所有Python对象都必须通过pickle序列化再传到子进程去
      - 多线程和多进程最大的不同在于,多进程中,同一个变量,各自有一份拷贝存在于每个进程中,互不影响,而多线程中,所有变量都由所有线程共享,所以,任何一个变量都可以被任何一个线程修改,因此,线程之间共享数据最大的危险在于多个线程同时改一个变量,把内容给改乱了。
      - 因为Python的线程虽然是真正的线程,但解释器执行代码时,有一个GIL锁:Global InterpreterLock,任何Python线程执行前,必须先获得GIL锁,然后,每执行100条字节码,解释器就自动释放GIL锁,让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁,所以,多线程在Python中只能交替执行,即使100个线程跑在100核CPU上,也只能用到1个核。
      - Python虽然不能利用多线程实现多核任务,但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁,互不影响。
    - 多线程
      - thread threading
      - t = threading.Thread(target=loop, name='LoopThread') t.start t.join
      - lock = threading.Lock()  lock.acquire()  lock.release()
    - ThreadLocal
      - local_dict = threading.Local() 存放各线程的局部变量
    - 进程和线程
      - 计算密集型 和 IO密集型
      - 充分利用操作系统提供的异步IO支持,就可以用单进程单线程模型来执行多任务,这种全新的模型称为事件驱动模型
      - 对应到Python语言,单进程的异步编程模型称为协程，有了协程的支持,就可以基于事件驱动编写高效的多任务程序。
    - 分布式进程
      - Python的 multiprocessing 模块不但支持多进程,其中 managers 子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者,将任务分布到其他多个进程中,依靠网络通信
- 常用内建模块
    - collections
      - namedtuple:Point = namedtuple('Point', ['x', 'y']) # namedtuple('名称', [属性list])
      - deque是为了高效实现插入和删除操作的双向列表,适合用于队列和栈
      - defaultdict:defaultdict(lambda: 'N/A') key不存在时返回默认值
      - OrderedDict:key保持插入时的顺序
      - Counter：计数器，实际上也是dict的一个子类
- Web开发
    -
    - WSGI:Web Server Gateway Interface
    - 无论多么复杂的Web应用程序,入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过 environ 获得,HTTP响应的输出都可以通过 start_response() 加上函数返回值作为Body。
- 协程
    - 
    - 协程的特点在于是一个线程执行
    - 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换,而是由程序自身控制,因此,没有线程切换的开销
    - 第二大优势就是不需要多线程的锁机制,因为只有一个线程,也不存在同时写变量冲突,在协程中控制共享资源不加锁,只需要判断状态就好了,所以执行效率比多线程高很多。
    - gevent是第三方库,通过greenlet实现协程