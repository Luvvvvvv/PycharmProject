import matplotlib.pyplot as plt
import numpy as np

"""
np.random.normal(loc=0.0, scale=1.0, size=None)
作用：生成高斯分布的概率密度随机数
参数解释：
loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
size：int or tuple of ints
    输出的shape，默认为None，只输出一个值
"""
# x and y must be the same size
x=np.random.normal(0,1,10) # 10表示输出散点的个数，也即size
y=np.random.normal(0,1,10)
# x和y必然成对出现
# x1 and y1 must be the same size
x1=np.random.normal(0,1,10)
y1=np.random.normal(0,1,10)

plt.figure() # 给我一张纸
plt.scatter(x,y,c='r',label='abc')  #绘制散点图
plt.scatter(x1,y1,c='g',label='RXX')
plt.legend() #给图像加上图例，即贴上label='abc'和label='RXX'标签
plt.show() #展示图像
