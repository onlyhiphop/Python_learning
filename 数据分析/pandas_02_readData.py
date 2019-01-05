import pandas as pd

text_csv = pd.read_csv("./US_video_data.csv")  # 返回DataFrame对象
print(text_csv)

print("="*20)
print(text_csv.head(2))


