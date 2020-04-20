#添加元素 插入元素
number=[1,2,3,4,5]
number.append(6)
number.extend([7,8,9,10])
number.insert(2,0)
number.insert(0,0)
print(number)

#查询 与 调换元素顺序
name=["egg","1","beef","2"]
print(name[0],name[2])
name[1],name[3]=name[3],name[1]
print(name)

#删除元素
name=["egg","1","beef","2"]
name.remove("1")
del name[2]
print(name)

#弹出元素
name=["egg","meat","beef","fish"]
print(name.pop(2))

#列表分片
name=["egg","meat","beef","fish"]
print(name[:2])
print(name[1:])
print(name[3:])
print(name[:])

#列表进阶分片
list=[1,1,1,2,3,4,5,6,7,8,9]
print(list[0:9:3])
print(list[::-1])
print(list.count(1))
print(list.index(2))
list.reverse()
print(list)