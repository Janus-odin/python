# 格式化输出
print('开始——————————')
print('2222')
print('2222')
print('22222')
print('2222')
print('2222')

print('结束——————————')

# %s 占位 ，稍后会填写
# %d 在字符串中占位数字 digit
# %f 在字符串中占位小数
print("我叫%s,今年%d,收入%f" %('zjan',15,3.3))

# 新的格式化方案。f-string
name = 'zhang'
age = 23
hobby='aaa'
print(f"我叫{name}, {age}, {hobby}")