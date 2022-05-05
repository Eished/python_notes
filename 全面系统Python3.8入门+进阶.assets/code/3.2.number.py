print(type(1))
print(type(-1))
print(type(1.1))
print(type(1.1111111111111111111111111111))
print(type(1 + 0.1))
print(type(1.0 + 1))
print(type(1.0 * 1))
print(type(1 / 1))  # <class 'float'>
print(type(1 // 1))  # <class 'int'>
print(1 // 2)  # 0
print(1 / 2)  # 0.5

# 二进制
print(0b11)  # 3
# 八进制
print(0o11)  # 9
# 十六进制
print(0x1f)  # 31

# 进制转换
# 转换为二进制
print(bin(0x1f))  # 0b11111
# 转换为八进制
print(oct(0x1f))  # 0o37
# 转换为十进制
print(int(0x1f))  # 31
# 转换为十六进制
print(hex(0b11111))  # 0x1f

# boolean
print(type(True))
print(type(False))
print(int(True))  # 1
print(int(False))  # 0
print(bool(1))  # True
print(bool(0))  # False
print(bool(1.1))  # True
print(bool(-1.1))  # True
print(bool(0b01))  # True
print(bool(0b00))  # False
print(bool(''))  # False
print(bool('a'))  # True
print(bool([1, 2]))  # True
print(bool([]))  # False
print(bool({1, 2, 3}))  # True
print(bool({}))  # False
print(bool(None))  # False
# 复数
print(360432j)  # False
