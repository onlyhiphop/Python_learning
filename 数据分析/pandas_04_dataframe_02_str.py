"""
    1. DataFrame的条件选择
    2. pandas的字符串方法
"""
import pandas as pd

person_dict = {
    "name": ["zhangsan", "lisi", "wangwu"],
    "age": [18, 19, 20],
    "tel": ["1000", "2000", "3000"]
}

df = pd.DataFrame(person_dict)

# 选择条件
fd = df[df["age"] > 18]
print(fd)
# 多个条件  用 & 连接
# 注意：要用 () 括起来
fd2 = df[(18 < df["age"]) & (df["age"] < 20)]
print(fd2)


"""
    常用的pandas之字符串方法:
    str.cat : 实现元素级的字符串连接操作，可指定分隔符
    str.contains: 返回表示各字符串是否含有指定模式的布尔型数组
    str.count : 模式的出现次数
    str.endswith/startswith : 相当于对各个元素执行 x.endswith() 和 x.startswith()
    str.findall : 计算各字符串的模式列表
    str.get : 获取各元素的第i个字符
    str.join : 根据指定的分隔符将Series中各元素的字符串连接起来
    str.len : 计算各字符串的长度
    str.lower/upper : 转换大小写，相当于对各个元素执行 x.lower()  x.upper()
    str.match : 根据指定的正则表达式对各个元素执行re.match
    str.pad : 在字符串的左边，右边或左右两边添加空白符
    str.center : 相当于pad(side="both")
    str.repeat : 重复值，列如 s.str.repeat(3) 相当于对各个字符串执行重复三次
    str.replace : 用指定字符串替换找到的模式
    str.slice : 对Series中的各个字符串进行子串截取
    str.split : 根据分隔符或正则表达式对字符串进行拆分
    str.strip/rstrip/istrip : 去除空白符，包括换行符，相当于对各个元素进行x.strip() x.rstrip() x.istrrip()
    
"""
person_list = [
    {
        "name": "zhangsan",
        "age": 18,
        "hobbies": "reading/running/movie/traveling"
    },
    {
        "name": "lisi",
        "age": 19,
        "hobbies": "eating/traveling/fishing"
    },
    {
        "name": "wangwu",
        "age": 20,
        "hobbies": "basketball/pingpang"
    }
]
df_list = pd.DataFrame(person_list)
# str.split() 的使用
df_split = df_list["hobbies"].str.split("/")  #
print(df_split)
print(type(df_split))  # <class 'pandas.core.series.Series'>
# 可以用tolist方法将 Series对象转换成List
print(df_split.tolist())

# str.replace() 的使用
df_repl = df_list["hobbies"].str.replace("/", ",")
print(df_repl)
