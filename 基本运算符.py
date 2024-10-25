# # bytes 类型
#
# s = "中国"# 内存中使用的是unicode
#
# # 编码
#
# bs = s.encode('utf-8')  # <class 'bytes'>  bytes 类型
# # b'\xe4\xb8\xad\xe5\x9b\xbd'   每个 /x 是一个字节
#
# print(bs)
# print(type(bs))
from encodings.utf_7 import encode

#  把字节转换回字符串

bs = b'\xe4\xb8\xad\xe5\x9b\xbd' #
s = bs.decode('utf-8')
print(s)

# 不同编码之间是不能直接转换的。
# encode 编码
# decode 解码

# byte - 8个01