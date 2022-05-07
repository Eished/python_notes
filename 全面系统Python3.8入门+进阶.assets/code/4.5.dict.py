print(type({}))
print({1: 1, 2: 2, 3: 3})
print({1: "a", 2: "b", 3: "c"})

dict1 = {"q": "aaa", "w": "bbb", 3: "ccc"}
print(dict1["q"])
print(dict1[3])

# key 支持大部分不可变类型
dict2 = {("q", 2): "qqq222", "w": "bbb", 3: "ccc"}
print(dict2[("q", 2)])
