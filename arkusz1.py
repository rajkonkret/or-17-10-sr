import pandas as pd
import numpy as np
import openpyxl

# pip install pandas
technologies = ['Spark', 'Pandas', "Java", 'Python', 'PHP']
fee = [25000, 2000, 15000, 15000, 18000]
duration = ['50 Days', '35 Days', np.nan, '30 Days', '30 Days']
discount = [2000, 1000, 500, 800, 500]
columns = ['Courses', 'Fee', 'Duration', 'Discount']

df = pd.DataFrame(list(zip(technologies, fee, duration, discount)), columns=columns)

print(df)
#   Courses    Fee Duration  Discount
# 0   Spark  25000  50 Days      2000
# 1  Pandas   2000  35 Days      1000
# 2    Java  15000      NaN       500
# 3  Python  15000  30 Days       800
# 4     PHP  18000  30 Days       500

df.to_excel('Courses.xlsx', index=False)
