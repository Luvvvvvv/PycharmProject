from time import sleep

print('---------------------植物拍摄教程---------------------')
print('根据结果我们发现拥有构图的照片的满意度普遍比没有构图的高')
print(' 在此推荐拍摄植物都使用黄金螺旋线的构图,以突出植物本体')
temp = input('      请选择你拍摄的主要影响因素(1.视角)(2.光线)')
i = int(temp)
if (i < 1 or i > 2):
    print('----------------------输入错误------------------------')
if i == 1:
    print('                 ‘你选择了视角为主体’')
    temp1 = input('------请选择你的拍摄角度(1.平拍)(2.俯拍)(3.仰拍)------')
    j = int(temp1)
    if (j < 1 or j > 3):
        print('----------------------输入错误------------------------')
    if j == 1:
        print('                    ‘你选择了平拍’')
        print('                  ‘推荐使用顺光拍摄’')
    if j == 2:
        print('                    ‘你选择了俯拍’')
        print('                  ‘推荐使用顺光拍摄’')
    if j == 3:
            print('                    ‘你选择了仰拍’')
            print('                  ‘推荐使用顺光拍摄’')
if i == 2:
    print('                 ‘你选择了光线为主体’')
    temp2 = input('----------请选择你的拍摄光线(1.顺光)(2.逆光)-----------')
    j = int(temp2)
    if (j < 1 or j > 2):
        print('----------------------输入错误------------------------')
    if j == 1:
        print('                    ‘你选择了顺光’')
        print('                 ‘推荐使用平拍或俯拍’')
    if j == 2:
        print('                    ‘你选择了逆光’')
        print('                 ‘推荐使用平拍或仰拍’')

sleep(5)
