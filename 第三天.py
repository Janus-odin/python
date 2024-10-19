# 缩进与注释
# 在pyton 中一个缩进等于四个空格
from curses.ascii import isdigit

# python 不使用 {} 来控制 类 函数。逻辑判断  而是使用缩进
# if True:
#     print(True)
# else:
#     print(False)


# python 使用多行
# Python 中一般以新行作为语句的结束标识，可以使用 \ 将一行语句分为多行显示。如下所示：

a = 128
b = 1024
c = 512
d = a + \
    b - \
    c
print(d)

# 如果包含在 []、{}、() 括号中，则不需要使用 \。如下所示：
arr = {
    a,
    b,
    c
}
print(arr)


# Python 中单行注释使用 #，多行注释使用三个单引号（'''）或三个双引号（"""）。如下所示：

# 我是单行注释

'''
我是多行注释
我是多行注释
'''

"""
我是多行注释
我是多行注释
"""
# 数据类型

"""
整数：可以为任意大小、包含负数

浮点数：就是小数

# 字符串：以单引号 '、双引号"、三引号 /''' 或 /""/" 括起来的文本

布尔：只有 True、False 两种值

空值：用 None 表示

变量：是可变的

常量：不可变
"""


# 常用运算符

"""
+	相加	a + b
-	相减	a - b
*	相乘	a * b
/	相除	a / b
%	取模	a % b
**	幂	a**b 表示 a 的 b 次幂
//	取整除	9 // 4 结果为 2
==	是否相等	a == b
!=	是否不等于	a != b
>	是否大于	a > b
>=	是否大于等于	a >= b
<=	是否小于等于	a <= b
=	简单的赋值运算符	a = b + c
+=	加法赋值运算符	a += b 等效于 a = a + b
-=	减法赋值运算符	a -= b 等效于 a = a - b
*=	乘法赋值运算符	a *= b 等效于 a = a * b
/=	除法赋值运算符	a /= b 等效于 a = a / b
%=	取模赋值运算符	a %= b 等效于 a = a % b
**=	幂赋值运算符	a **= b 等效于 a = a ** b
//=	取整除赋值运算符	a //= b 等效于 a = a // b
&	与	a & b
|	或	a | b
^	异或	a ^ b
~	取反	~a
<<	左移动	a << 3
>>	右移动	a >> 3
and	布尔类型与	a and b
or	布尔类型或	a or b
not	布尔类型非	not a
is	判断两个标识符是否引用同一个对象	a is b
is not	判断两个标识符是否引用不同对象	a is not b
"""
a=1
b=2
print(b>0 or b>2)


# 运算符优先级
"""

运算符
描述（由上至下对应优先级由高到低）
** 幂运算
~ + -    取反、正号、负号
* / % // 乘、除、取模、取整除
+ -    加法、减法
>> << 右移、左移
& 与
^ | 异或、或
<= < > >= 比较运算符
== != 是否等于、是否不等于
= %= /= //= -= += *= **= 赋值运算符
is is not 身份运算符
in not in 成员运算符
not and or 逻辑运算符
————————————————
"""


# 基本语句
# 1 条件语句

# 在进行逻辑判断时，我们需要用到条件语句，Python 提供了 if、elif、else 来进行逻辑判断。格式如下所示：
"""

if 判断条件1:
    执行语句1...
elif 判断条件2:
    执行语句2...
elif 判断条件3:
    执行语句3...
else:
    执行语句4...

"""
# name = input("请输入年龄")
# if name.isdigit():
#     if "60">name>"18":
#         print("你已经成人了")
#     elif  name>"18":
#         print("你老了")
#     else:
#         print("name")
#
# else:
#     print('请输入正确的数字')


# 2 循环语句
# 当需要多次重复执行时，我们要用到循环语句，Python 提供了 for 循环和 while 循环。
# for 循环可以遍历任何序列，比如：字符串。如下所示：

# str = 'Python'
# for s in str:
#     print(s)

# 2.2 while 循环
# while 循环，满足条件时进行循环，不满足条件时退出循环。如下所示：

# sum = 0
# m = 10
# while m > 0:
#     sum = sum + m
#     m = m - 1
#     print(sum)
# print(sum)

# 2.3 break
# break 用在 for 循环和 while 循环语句中，用来终止整个循环。如下所示：

# str = 'Python'
# for s in str:
#     if s == 'o':
#         break
#     print(s)

# 2.4 continue
# continue 用在 for 循环和 while 循环语句中，用来终止本次循环。如下所示：

#
# str = 'Python'
# for s in str:
#     if s == 'o':
#         continue
#     print(s)

# 3 pass 语句
# pass 是空语句，它不做任何事情，一般用做占位语句，作用是保持程序结构的完整性。如下所示：


# if True:
#     pass

