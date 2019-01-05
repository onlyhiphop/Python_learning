# coding = utf-8

"""
    折线图的绘制  .plot(x, y)
"""
from matplotlib import pyplot as plt

# x = []
# for a in range(2, 26, 2):
#     x.append(a)

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 24, 22, 18, 15, 13]

# print(x.__len__()) 要保持x ， y 一一对应

# 设置图片的大小以及清晰度
# figsize 图片的大小 (长，宽)   dpi 图片的清晰度
fig = plt.figure(figsize=(20, 18), dpi=80)

# 根据给出的x，y值进行绘图
plt.plot(x, y)

# 会发现一个问题 ， 它自动画的图 x，y轴不是我们设置的 ，是它自己的适应的
# 所以我们可以强制设置x轴 的精度 
_xtick_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xtick_labels[::3])  # 步数为三 遍历列表取出值

# 也可以调整y轴的精度
plt.yticks(range(min(y), max(y)+1))


# 如果要在x轴上 显示字符串  第一个参数是 x轴的精度， 第二个参数是要显示的字符串 必须要一一对应
_x = x[::2]
_xticks_label = ["hello.{}".format(i) for i in _x]
plt.xticks(_x, _xticks_label)

# 画网格 
plt.grid()

# 展示
plt.show()
# 注意 要保存图片就不能展示，否则保存的图片为空白

# 保存图片
# 还可以保存为 svg 这个矢量图片格式，放大不会有锯齿，在网页上不会失帧
# plt.savefig("./t1.png")
