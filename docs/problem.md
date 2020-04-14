# Collection of Python related issues

  - 安装第三方包缓慢的问题
    
    |镜像来源|url|
    |---|---| 
    |阿里云|https://mirrors.aliyun.com/pypi/simple/|
    |清华|https://pypi.tuna.tsinghua.edu.cn/simple/|
    |中科大|https://pypi.mirrors.ustc.edu.cn/simple/|
     - 临时更换镜像源
       - pip install -i url package_name
     - 永久更换镜像源
       - Windows:
         - 在C盘user（显示中文的就是用户）/[用户名] 目录下创建一个pip目录，在其下新建一个pip.ini文件。添加如下内容
         - ```python
            [global]
            index-url = https://mirrors.aliyun.com/pypi/simple/
            [install]
            trusted-host=mirrors.aliyun.com
           ```
       - Linux:
          - 在~(你的用户目录)下创建一个.pip目录，在下面创建一个pip.conf文件，添加相同的内容（如上Windows）即可。 
       - PyCharm:
          - settings --> project interpreter --> manage repositories
  - 转义字符
    - \r 将光标移到一行的开始,覆盖
    - \b 退格符,将光标前移,覆盖
  - mcs
    - 使用@staticmethod或@classmethod,就不需要实例化类对象，直接类名.方法名（）调用；有利于组织代码；
    - cls作为第一个参数用来表示类本身，类方法是只与类本身有关而与实例无关的方法
  - 字典中的中文乱码问题
    ```
    import json
    
    dict = {'标题':'这是标题'}
    print json.dumps(dict, ensure_ascii=False, encoding='UTF-8')
    ```
  - Markdown插件支持
    - [idea 插件库](https://plugins.jetbrains.com/)下载后不用解压，直接install plugins from disk
    - settings --> edit --> file type 修改各种文件类型
```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(mcs, x):
        mcs.val = x
        mcs.next = None

class Solution(object):
    def addTwoNumbers(mcs, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        cur_l1, cur_l2 = l1, l2
        cur_node = dummy_head
        carry = 0  # 表示进位
        while cur_l1 is not None or cur_l2 is not None:
            x = (cur_l1.val if cur_l1 else 0)
            y = (cur_l2.val if cur_l2 else 0)
            sum_val = x + y + carry
            carry = sum_val / 10
            cur_node.next = ListNode(sum_val % 10)
            cur_node = cur_node.next
            cur_l1 = (cur_l1.next if cur_l1 else None)
            cur_l2 = (cur_l2.next if cur_l2 else None)
        if carry > 0:
            cur_node.next = ListNode(carry)
        return dummy_head.next
```

   - __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
   - __all__属性 由string元素组成的list变量，指定该模块可导出的类，函数，变量；且只影响from <module> import *这种方式，具体的指定导入并没有影响。
  