def discounts(price, rate):
    final_price = price * rate
    print('打印全局变量', old_price)
    return final_price


old_price = float(input('原价：'))
rate = float(input('折扣：'))
new_price = discounts(old_price, rate)
print("打折后：", new_price)
