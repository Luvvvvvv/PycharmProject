def test(*params):
    print("有%d个参数" % len(params))
    print("第3个参数是", params[2])
test('f', 'd', 'a', 'c', 'e')
