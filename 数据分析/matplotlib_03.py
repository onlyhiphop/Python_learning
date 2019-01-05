"""
    画两个图比较
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager


# 设置字体
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

x = range(10, 20)
y_1 = [1, 2, 5, 5, 3, 4, 2, 2, 1, 1]
y_2 = [2, 1, 3, 3, 5, 4, 2, 1, 1, 1]

# 给每条线加上一个标注， 使用label参数 ，还不够
plt.plot(x, y_1, label="目标1", color="orange")
plt.plot(x, y_2, label="目标2", color="cyan")

# 与上面对应： 添加图例（每条线的意思）
# 注意 ： 只有这里添加字体参数是 prop
# loc 参数控制位置
plt.legend(prop=my_font, loc="upper left")

_xticks = ["{}岁".format(i) for i in x]
plt.xticks(x, _xticks, fontproperties=my_font)

plt.xlabel("岁数", fontproperties=my_font)
plt.ylabel("女朋友", fontproperties=my_font)

plt.show()
