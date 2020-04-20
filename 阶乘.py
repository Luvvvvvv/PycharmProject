def recursion(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


number = int(input("input a num"))
result = recursion(number)
print("%d的阶乘是：%d" % (number, result))

