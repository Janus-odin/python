# 字符串添加 对原来的字符串不影响
from os import remove

# 数组进行添加 会改变原来的数据
# append 效率高 insert 效率低

lst = ["zhoujielun","xiaoming"]

lst.insert(0,'hahaha')
print(lst)

lst.append('zzt')
print(lst)

# extend   迭代新增
n = [1,2,3]
lst.extend(n)
print(lst)


#列表删除
# remove()

lkt = ['haha','hehe','heihei']
lkt.remove('haha')  #删除某个元素
print(lkt)

# range    给list。循环使用的。
