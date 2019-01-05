"""
    numpy中的nan和inf
    nan: 表示不是一个数字，注意是 float类型才有nan
        1. 当我们读取本地的文件为float的时候，如果有缺失，就会出现nan
        2. 当做了一个不合适的计算的时候（比如无穷大（inf）减去无穷大）

    nan与任何数运算都等于 nan

    inf：表示正无穷
    -inf：表示负无穷
"""

import numpy as np

# 1. 两个nan是不相等的
print(np.nan == np.nan)  # False

# 2. 可以利用两个nan相等的特性来判断数组中nan的个数
t = np.arange(24).reshape(4, 6)

t[:, 0] = 0  # 将第一列都变成0

# 此处出现错误， nan是float类型的 所以要转化
t = t.astype("float")
t[1, 1] = np.nan  # 将第二行第二列的元素变成nan
t[2, 2] = np.nan
print(t)

# .count_nonzero()
print(np.count_nonzero(t))  # 不为0的元素的个数
print(np.count_nonzero(t != t))  # 找出里面的 nan （因为只有nan不等于nan）
print(t != t)  # 返回一个数组，nan处的为 True  不为nan为 False

# .isnan(numpy) 返回一个bool类型的数组，nan处为true
print(np.isnan(t))

# 里面存在nan ， 所以得到nan
print(np.sum(t))


"""
    在一个数组中存在nan，就无法算出某行或某列的，均值。
    解决：将里面的nan变成要计算的某行或某列的 均值或中值
"""
