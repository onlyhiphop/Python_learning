"""
    1. 数组的拼接
        1.1 竖直拼接  np.vstack((t1, t2))
        1.2 水平拼接  np.hstack((t1, t2))
        注意：竖直分割和水平分割 与 拼接对应，是互逆的
"""

import numpy as np

# vs = np.arange(12).reshape((3, 4))
# vs_2 = np.arange(12, 24).reshape((3, 4))

# vs_3 = np.vstack((vs, vs_2))
# hs = np.hstack((vs, vs_2))
# print(vs)
# print(vs_2)
# print(vs_3)
# print(hs)


"""
    2. 数组的行列交换
"""
# print(vs)
# 把第一行和第二行互换
# vs[[0, 1], :] = vs[[1, 0], :]
# print(vs)

# 把第一列和第二列互换
# vs[:, [0, 1]] = vs[:, [1, 0]]
# print(vs)


file_path = "./US_video_data.csv"
text = np.loadtxt(fname=file_path, dtype="int", delimiter=",")

# 往文件中拼接一列全为0的数组
# .zeros() 参数为一个元组，表示行和列
# 该方法生成一个 全为 0 的数组，类型是 float 所以转换成int
z = np.zeros((text.shape[0], 1)).astype("int")

# 拼接
# 将 z 和 text 行拼接
text_z = np.hstack((text, z))


# .ones() 参数为一个元组，生成一个全为1 的数组
o = np.ones((1, text_z.shape[1])).astype("int")
# 将 p 和 text 列拼接
text_z = np.vstack((text_z, o))
print(text_z)

# .eye() 创建一个方阵 对角线为
e = np.eye(10)
# print(e)

# .argmax( , axis=)  找出某轴上最大值， 返回其所在轴的索引
# .argmin() 对应的方法
max_index = np.argmax(e, axis=0)
min_index = np.argmin(e, axis=0)
print(max_index)
print(min_index)

# .sum(numpy)  求这个数组的全部和
# .sum(, axis=) 求 在某轴上的和
s = np.sum(e, axis=0)  # 每一行相加， 返回一个1行的数据

# .ptp()  .ptp(, axis=)  求极值（最大值-最小值）
# .std()  .std(t, axis=)  求标准差（一组数据平均值分散程度的一种度量， 越大表示波动越大，越不稳定）

# .random.randint(low, high, (shape)) 随机创建一个 在[low,high) 内的数 的随机数组
rin = np.random.randint(10, 20, (4, 5))
print(rin)

# .random.rand(shape)  创建均匀分布的随机数组，float类型，范围0-1
rand_1 = np.random.rand(2, 3)
print(rand_1)

# random.seed(s)  随机数种子，s是给定的种子数
# 在前面给定之后， 后面产生的随机数 ，都是第一次产生的，后面不会再随机
np.random.seed(1)
print(np.random.randint(0, 10, (2, 3)))
print(np.random.randint(0, 10, (2, 3)))


"""
    numpy的注意点  copy 和 view
    1. a = b 完全不复制， a 和 b 相互影响
    2. a = b[:] , 视图的操作，一种切片，会创建新的对象a，但是a的数据
        完全由b保管，他门两个的数据变化是一致的
    3. a = b.copy() 复制， a 和 b 互相不影响
"""
a = np.arange(10).reshape((2, 5))
b = a
b[b > 5] = 1
print(b)
print(a)  # a 也会改变

c = a[:]
c[c > 5] = 1
print(c)
print(a)  # a 的值也会改变

d = a.copy()
d[d > 5] = 0
print(d)
print(a)  # a 的值不会改变

