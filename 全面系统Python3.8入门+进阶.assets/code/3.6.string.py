print("1")
print('1')
print(1)

print(type("1"))  # <class 'str'>
print(type('1'))  # <class 'str'>
print(type(1))  # <class 'int'>

print('let\'s go')
print("let's go")

print('''let's go 1, 
1, 
1''')

print("""let's go 2, 
2, 
2""")

# 使用反斜杠n换行
print("""let's go 3, \n3, \n3""")

print("let's go 4, \n4, \n4")

# 使用三引号换行，多两个回车
print("""
let's go 5, 
5, 
5
""")

# 使用反斜杠换行输入，实际并没有换行
# let's go 6, 6, 6
print("\
let's go 6, \
6, \
6\
")

# 转义字符
print('1\n1')
print('2\`2')
print('3\t3')
print('4\r4')
print('hello \n world')
print('hello \\n world')  # hello \n world
