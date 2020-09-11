import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_excel(
    r"C:\Users\motei\Desktop\2017年研究生数学建模竞赛优秀论文选\2017年优秀论文\A\附件1 区域高程数据.xlsx", header=None)
dataArray = np.array(data)
# print(dataArray[0,0])
size = dataArray.size  # 获取矩阵中元素个数
shape = dataArray.shape  # 获取矩阵维度
x = np.arange(0, shape[0]*38.2/1000, 38.2/1000)  # 这里不用-1注意
y = np.arange(0, shape[1]*38.2/1000, 38.2/1000)
xx, yy = np.meshgrid(x, y)  # 把x,y数据生成mesh网格状的数据，因为等高线的显示是在网格的基础上添加上高度值
# print(xx.shape,yy.shape)
fig = plt.figure()
ax = Axes3D(fig)
# 当 X,Y,Z 都是 2 维数组时，它们的形状必须相同。
ax.plot_surface(xx, yy, dataArray.transpose(),
                rstride=1, cstride=1, cmap=cm.viridis)
# print(size)
plt.show()

# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)
# plt.show()
