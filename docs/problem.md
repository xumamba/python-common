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