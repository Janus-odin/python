# 1.编译型语言和解释型语言的区别

# 编译型语言写的程序在执行之前，需要一个专门的编译过程，把程序编译成机器语言的文件 ，执行效率高

# 解释型语言就是程序不需要编译，程序在运行的时候才需要编译，每执行一次都要翻译一次，跨平台性好

# 2.环境安装

 # 去python 官网进行下载 python 配置环境。 下载python 的编写工具


# 3.语句分隔符
#在python中通常使用换行符作为语句分隔符，每个语句单独占一行
# 4.注释语句
#python中的注释是用来解释代码的，分为单行注释和多行注释
# 单行注释使用# 多行注释使用""" """  三双引号

# 这是单行注释

"""
这个是多行注释
可以写多行的内容



"""

# 5.pep8规范

"""
pep8规范包含如下几条
缩进：使用四个空格表示缩进
行长：每行应该不超过79个字符
命名规则：变量名应该以小写字母开头，使用下划线分隔多个单词，类名要以大写的字母开头，使用驼峰命名
空格：在运算符两侧、逗号后、以及冒号后应添加空格
函数和类：函数和类之间应该用两个空行分隔
导入：每个导入应该使用一行，避免使用通配符导入

"""
a = 11
b = '23'
print(a+int(b))