# fromkeys() 创建并放回一个新字典
dict1 = {}
print(dict1.fromkeys((1, 2, 3)))

# keys() 返回字典中的键
dict2 = {}
dict2 = dict1.fromkeys(range(5), "yes!")
print(dict2.keys())

# values() 返回字典中的值
print(dict2.values())

# items() 返回字典中的键值对
print(dict2.items())

# get()访问字典项
print(dict2.get(0))
print(dict2.get(5, "nope"))

print(5 in dict2)
print(2 in dict2)

# clear()
dict2.clear()
print(dict2)

# copy()
a = {1: "one", 2: "two"}
b = a.copy()
print(b)

# pop() popitem()
a = {1: "one", 2: "two"}
print(a.pop(1))
print(a.popitem())

# update
a = {'zlm': "one", 'ljw': "two"}
a.update(ljw="three")
print(a)
