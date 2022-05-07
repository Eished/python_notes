print('hello'+"world")
# 相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并
print('hello' "world")
print('hello'*2)
print('hello'[4])
print('hello'[0])
print("hello world"[6])
# 用负数索引时，从右边开始计数
print("hello world"[-5])

# 截取字符串 包含切片开始，但不包含切片结束,多数一位
print("hello world"[0:5])  # hello
print("hello world"[0:-1])  # hello worl

# 截取world 冒号前面默认0，后面默认最后一位位置
print("hello world"[6:11])  # world
print("hello world"[6:])  # world
print("hello world"[-5:])  # world
