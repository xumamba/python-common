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
    - set之间 交（&） 并（|）集 
    - 对于不变对象来说,调用对象自身的任意方法,也不会改变该对象自身的内容。相反,这些方法
会创建新的对象并返回,这样,就保证了不可变对象本身永远是不可变的。

- IO编程
    -
    - 操作系统同一时间能打开的文件数量也是有限的
    - ```python
       with open('/path/to/file', 'r') as f:
          print f.read()
      ```
- 进程和线程
    -
    - multiprocessing
    - 进程间通信
      - Queue
      - 多线程和多进程最大的不同在于,多进程中,同一个变量,各自有一份拷贝存在于每个进程中,互不影响,而多线程中,所有变量都由所有线程共享,所以,任何一个变量都可以被任何一个线程修改,因此,线程之间共享数据最大的危险在于多个线程同时改一个变量,把内容给改乱了。
      - 因为Python的线程虽然是真正的线程,但解释器执行代码时,有一个GIL锁:Global InterpreterLock,任何Python线程执行前,必须先获得GIL锁,然后,每执行100条字节码,解释器就自动释放GIL锁,让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁,所以,多线程在Python中只能交替执行,即使100个线程跑在100核CPU上,也只能用到1个核。
      - Python虽然不能利用多线程实现多核任务,但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁,互不影响。
      - 计算密集型 和 IO密集型
      - 充分利用操作系统提供的异步IO支持,就可以用单进程单线程模型来执行多任务,这种全新的模型称为事件驱动模型
      - 对应到Python语言,单进程的异步编程模型称为协程
      - Python的 multiprocessing 模块不但支持多进程,其中 managers 子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者,将任务分布到其他多个进程中,依靠网络通信。
      
- Web开发
    -
    - WSGI:Web Server Gateway Interface
    - 无论多么复杂的Web应用程序,入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过 environ 获得,HTTP响应的输出都可以通过 start_response() 加上函数返回值作为Body。
    - 
    