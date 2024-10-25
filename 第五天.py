# while 循环

# num = 100
#
# while num>0 :
#     print(num)
#     num-=1

# while 条件式循环。 for  序列式循环
str = 'hello'

# for i in str:
#     print(i)
#     print(len(str) )

# for i in [1,23,43,2,2.3,444]:
#     print(i)

# for i in [1,2,3,4,5,6,7,8,9]:
#     print(i)

# range  列表
# for i in range(1,99):
#     print(i)

# for i in range(1,99,3):
#     print(i)

# 随机验证码

# import random
# import string
#
#
# print(string.ascii_lowercase)  #小写字母
# print(string.ascii_uppercase) # 大写字母
# print(string.digits)  #数字
#
# allString = string.ascii_lowercase+string.ascii_uppercase+string.digits
#
# # print(randomnum)
# suijinum = ''
# for i in range(32):
#     randomnum = random.choice(allString)
#     suijinum=randomnum +suijinum
# print(suijinum)


# 累加和

# totle = 0
#
# for i in range(1,101):
#     totle = totle + i
# print(totle)


# 计算1-100 所有 偶数和

# totle = 0
# for i in range(0,100,2):
#     print(i)
#     totle = totle+i
#
# print(totle)


# 退出循环。break。 continue 退出当次循环

# while

# 常量
# python中不存在绝对的常量。约定：字母都是大写的 被默认当成为常量