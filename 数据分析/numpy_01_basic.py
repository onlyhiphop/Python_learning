"""
什么是Numpy
    一个python中做科学计算的基础库，重在数值计算，也是大部分PYTHON科学计算库的基础库，
    多用于在大型，多维数组上执行数值运算
"""
import numpy as np
import random

# 使用numpy 生成数组
# 使用 .array 方法
t1 = np.array([1, 2, 3])
print(t1)    # [1 2 3]
print(type(t1))  # <class 'numpy.ndarray'>

# 生成 0-9 的数组
t2 = np.array(range(10))
print(t2)
t3 = np.arange(10)
print(t3)

# .dtype : 查看数组的类型
print(t3.dtype)   # int32 类型

# dtype参数  "i1" 代表 int8  1位字节
t4 = np.arange(10, dtype="i1")
print(t4)
print(t4.dtype)

# dtype = bool类型
t5 = np.array([1, 0, 0, 1], dtype=bool)
print(t5)   # [ True False False  True]
print(t5.dtype)  # bool

# .astype: 将 t5 调回int8 类型
t6 = t5.astype("i1")  # 或 'int8'
print(t6)
print(t6.dtype)

# .round: 精确到多少位 四舍五入
t7 = np.array([random.random() for i in range(6)])
print(t7)
print(t7.dtype)
t8 = np.round(t7, 2)  # 取两位小数 和python中一样
print(t8)

# .shape ： 返回一个元组
# 对于一维数组来说：表示列数
# 对于二维数组来说：第一个表示行数，第二个表示列数
# 对于三维数组来说：第一个是快数，第二个是每个块的行数，第三个是每个块的列数
# 元组有几个数 ， 就表示是几维数组
t9 = np.array([[1, 2, 3], [4, 5, 6]])
print(t9.shape)  # (2, 3)    表示2行3列

tt1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(tt1)
print(tt1.shape)


# .reshape() : 传入一个元组可变成元组描述的样子
# 注意：该方法有返回值
tt2 = np.arange(12)
tt2 = tt2.reshape((3, 4))  # 变成3行4列
print(tt2)
print(tt2.shape)

# 3种数组的转置（行变成列，列变成行）
# 1 .transpose()
# 2 .T  一个属性
# 3 .swapaxes()
# 注意也是有返回值的，不是在原数组操作
tt2 = tt2.transpose()
print(tt2)
print(tt2.T)
print(tt2.swapaxes(1, 0))  # 0轴和1轴互换

# 24 = 2*3*4
tt3 = np.arange(24).reshape((2, 3, 4))
print(tt3)

# 注意 1行 6列 也是二维的 写法 多一个[]
tt4 = np.arange(6).reshape((1, 6))
print(tt4)

# 将一个不知道的几维数组转化成一维数组
# 方法1   将元组 全部项相乘
tt6 = tt2.reshape((tt2.shape[0]*tt2.shape[1], ))
print(tt6)

# 方法2  .flatten() 直接将一个数组变成一维数组
tt1 = tt1.flatten()
print(tt1)

# 二维数组的算法 就是矩阵的算法
# 加法： 每一项都加  乘法 除法 也是
tt7 = np.array([[1, 2, 3], [4, 5, 6]])
tt7 = tt7 + 2
print(tt7)
sum_tt = tt7**2  # 平方也是
print(sum_tt)
sum_tt2 = sum_tt * tt7
print(sum_tt2)

# 算法的特殊 除以0
# tt8 = tt7 / 0
# print(tt8)    # inf 表示无限   nan 表示 不是个数组，不存在

# 不同维数的数组也可以进行 加减乘除
# 但只能列数对应 ， 用多维数组的每一行去对低维数组做运算
a1 = np.array([1, 2, 3, 4, 5, 6])
a2 = np.arange(1, 25).reshape((4, 6))
print(a2)
print(a2 - a1)

# 行数对应， 用a2 的每一列去减去 a3的唯一一列
a3 = np.arange(4).reshape(4, 1)
print(a3)
print(a2 - a3)