import pandas as pd

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)     # 显示所有行

pd.set_option('display.float_format', lambda x: '%.2f' % x)  # 设置浮点数的显示格式