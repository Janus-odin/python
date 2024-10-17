# 1.字符串内置方法：
# upper 将字符串中的所有字符 全部转换为大写
from curses.ascii import isdigit
from pickletools import string4

s1 = "hello world"
# 只要是数据类型的内置方法 可以使用。数据类型.方法名（参数） 来使用
s2 =  s1.upper()
print(s2)

# lower 将字符串转成小写的
s3 = 'hhdkkKKKMM'
print(s3.lower())


# startswith endswith

s4 = "hello world banana"
print(s4.startswith("hel"))   # 字符串以什么开头

s5 = "www.baidu.com/a/b/c/a.png"
s6 = "www.baidu.com/a/b/c/b.jpg"
s7 = "www.baidu.com/a/b/c/c.webp"

print(s5.endswith('jpg'))


# 判断是不是数字字符串。isdigit（）
print("122ttt".isdigit())


# strip  去除字符串两端的空格


# 分隔
citys = "北京 哈尔滨 深圳"



# 运算符

# 语句 = 变量赋值 +运算符

# 计算运算符   + - *。/。   %

# %。取余

# 比较运算符 > < ==  <= >=  !=
#  返回值为 true。false

# 赋值运算符
# =
# 逻辑运算符
#  & ｜｜
# 成员运算符
