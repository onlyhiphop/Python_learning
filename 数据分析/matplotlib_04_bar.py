"""
    条形图的绘制:
        1. 正常的条形图 .bar()   粗细调整为 width
        2. 横着的条形图 .barh()  粗细调整为 height
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变性金刚5：最后的骑士"]
b = [56.01, 26.94, 17.53, 16.49, 15.45]

# 设置图形的大小
plt.figure(figsize=(20, 12), dpi=80)

# width : 设置条形图的宽度
plt.bar(range(len(a)), b, width=0.1)

# 设置x轴精度
plt.xticks(range(len(a)), a, fontproperties=my_font, rotation=45)

plt.show()

"""
    多个条形图的绘制:
        注意点，x后需要往右移
"""
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士"]
c = [23.23, 15.26, 13.28, 11, 8.65]
d = [26.51, 22.16, 26, 15.69, 18.77]

bar_width = 0.2

# 使他们的x轴 隔开  才不会重叠在一起
a_x = list(range(len(a)))
c_x = [i + bar_width for i in a_x]
d_x = [i + bar_width*2 for i in a_x]
plt.bar(a_x, b, width=bar_width, label="9月4日")
plt.bar(c_x, c, width=bar_width, label="9月5日")
plt.bar(d_x, d, width=bar_width, label="9月6日")

# 设置图例
plt.legend(prop=my_font)

# 调整精度，使x值 对应到条形的中间
plt.xticks(c_x, a, fontproperties=my_font)

plt.show()