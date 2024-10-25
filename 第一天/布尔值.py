# 布尔值只有 真 或 假
from curses.ascii import isdigit

# 最大的作用 用于判断
a=10
b=20

print(a>b)

# type  返回 数据类型

print(type(a))   # <class 'int'>


# input   # 给计算机互动。运行起来会等待用户输入 ，输入完之后会进行存储

name =  input('请输入你的名字')
print(name)
#  input 会出现的问题
# input 接受不了的所有数据都是  字符串


# 如何将字符串转化为 int   int(str)
# isdigit()  判断 是不是 字符串的数字


