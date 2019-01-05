"""
    散点图的绘制 .scatter(x, y)
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       21]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        15, 16]

x_3 = range(1, 31)
# 右移 好比较
x_10 = range(51, 81)
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘制散点图
plt.scatter(x_3, y_3, label="3月份")
plt.scatter(x_10, y_10, label="10月份")

# 添加图例
plt.legend(prop=my_font, loc="upper right")

# 调整x轴的刻度
_x = list(x_3) + list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i) for i in x_10]
# _x[::3]  步长为3的遍历
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)
plt.title("标题", fontproperties=my_font)

plt.show()