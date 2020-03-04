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
## 函数