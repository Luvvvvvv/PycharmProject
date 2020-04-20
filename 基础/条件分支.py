#条件分支
print(1 < 3)
print(1 > 3)
print(1 == 3)

print((3>2)and(3>1))
print((3>2)and(3<1))

temp = int(input("猜个数"))
guess = int(temp)
while guess!=8:
    temp = input("再猜个数")
    guess = int(temp)
    if guess==8:
        print("awesome")
    else:
        if guess>8:
            print("大了")
        else:
            print("小了")

