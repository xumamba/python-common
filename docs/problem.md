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
  - cls
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
  