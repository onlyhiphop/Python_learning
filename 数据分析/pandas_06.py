
import pandas as pd
from matplotlib import pyplot as plt

file_path = "./US_video_data.csv"

df = pd.read_csv(file_path)
# print(df)
# print(type(df))

# 点击量
click_data = df["点击量"].values
print(click_data)

# 设置组距 1000
j = 1000

# 计算组数
max_click = click_data.max()
min_click = click_data.min()
num_bin = (max_click - min_click) // j
print(num_bin)

# 设置图形的大小
plt.figure(figsize=(20, 10), dpi=80)

# 绘制直方图
plt.hist(click_data, num_bin)

# 设置精度
plt.xticks(range(min_click, max_click+5000, 5000))

plt.show()