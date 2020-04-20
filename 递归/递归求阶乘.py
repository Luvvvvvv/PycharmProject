def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("input a number"))
result = factorial(number)
print("%d的阶乘是：%d" % (number, result))
