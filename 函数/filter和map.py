def odd(x):
    return x % 2


temp = filter(odd, range(100))
print(list(temp))

print(list(filter(lambda x: x % 2, range(10))))

print(list(map(lambda x:x**2,range(6))))