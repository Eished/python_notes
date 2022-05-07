print(type((1, 2, 3)))
print(type(()))
print(type((1)))  # 无法识别成 tuple，括号二义性
print(type(("1")))  # 无法识别成 tuple
print(type((1,)))  # 正常识别
print(type(("1",)))  # 正常识别
