print(type({1, 2, 3, 4, 5}))
print(type({}))  # dict 无法识别成 set
print(type(set()))

# 无序、不重复
print({1, 2, 3, 4, 5})
print({1, 1, 2, 2, 3, 3, 4, 4, 5, 5})

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# 差集
print(set1 - set2)
# 交集
print(set1 & set2)
# 合集 并集
print(set1 | set2)
