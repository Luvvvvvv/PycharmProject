def funX(x):
    def funY(y):
        return x * y

    return funY


i = funX(8)
print(i(5))

print(funX(8)(5))


def funA():
    x=5
    def funB():
        nonlocal x
        x+=x
        return x
    return funB()

print(funA())