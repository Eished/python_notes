# append() 方法 可以在列表结尾添加新元素
arr = [1, 2, 3]
arr.append(4)
print(arr)

# 为切片赋值可以改变列表大小，甚至清空整个列表
arr2 = [1, 2, 3]
arr2 = [1, 2, 3, 4]
print(arr2)

# remove
arr2[1:3] = []
print(arr2)

# clear
arr2 = []
print(arr2)

# length
print((len(arr)))
