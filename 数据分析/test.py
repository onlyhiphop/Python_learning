# import pandas as pd
#
# file_path = "./json.txt"
#
# df = pd.read_json(file_path)
# print(df["data"].head(1).tolist())
# print(df.info())

import re

text = "hello world"
ret = re.match('he', text)

print(ret)
print(ret.group())
print(type(ret.group()))