"""
    直方图的绘制: .hist(列表,组数)
        0轴代表 数据  1轴代表出现的次数
        把数据分为多少组进行统计？
            组数要适当，太少会有较大的统计误差，大多规律不明显
            组距：指每个小组的两个端点的距离
            组数：极差 / 组距

     更多画图工具：  1. 百度echarts
                   2. plotly  https://plot.ly/python/
                   3. seaborn
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

a = [45, 84, 53, 56, 65, 55, 66, 95, 84, 62, 75, 48, 86, 100, 58, 96, 95, 75, 56, 82, 63, 55, 69, 87, 95, 68, 68,
     92, 72, 103]

# 设置组距
d = 5
# 计算组数
num_bins = (max(a) - min(a)) // d

# 设置图形的大小
plt.figure(figsize=(20, 10), dpi=80)

# 组距可以是个数列 ， 多个组距
# normed = True 可以将y轴变成频率
plt.hist(a, num_bins, normed=True)

# 设置x轴的刻度
# 因为range取不到最大值 所以加个组距
plt.xticks(range(min(a), max(a)+d, d))  # 步数为d

# 画网格
plt.grid()

plt.show()
