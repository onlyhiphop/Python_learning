# coding = utf-8

"""
    绘制 10点 到 11点 的温度变化图

    matplotlib默认不支持中文字符，因为默认的英文字体无法显示汉字

    查看Linux/mac 下面支持的字符
    fc-list -> 查看支持的字体
    fc-list :lang=zh -> 查看支持的中文（冒号前面有空格）

"""

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# 设置字体 (可以点进去看源码)
# 1.这个是window 和 Linux中设置的方式(这里是没用)
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc("font", **font)
# 上面等价于
# matplotlib.rc("font", family="MicroSoft YaHei", weight="bold", size="larger")

# 2. 设置字体(一定有用)   fname参数写字体资源的路径(此处为 微软雅黑 常规 的 文件路径)
# 一般用此种方法，一定有用，而且该变量可用于很多地方
my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")

x = range(0, 120)  # 返回range对象 是一个迭代器
y = [random.randint(20, 35) for i in range(120)]

# 设置图片的大小 清晰度
plt.figure(figsize=(15, 10), dpi=80)

plt.plot(x, y)

# 如果要在x轴上 显示字符串  第一个参数是 x轴的精度， 第二个参数是要显示的字符串 必须要一一对应
_x = list(x)
_xticks_label = ["10点{}分".format(i) for i in range(60)]
_xticks_label += ["11点{}分".format(i) for i in range(60)]
# rotation 旋转的度数
plt.xticks(_x[::10], _xticks_label[::10], rotation=90, fontproperties=my_font)


# 设置x，y轴的描述信息，以及标题
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位(℃)", fontproperties=my_font)
plt.title("10点到12点的气温变化情况", fontproperties=my_font)


plt.show()

# plt.savefig("./t2.png")
