from nicedate import nicedate
import matplotlib.pyplot as plt
#import datetime
import seaborn as sns
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.cbook as cbook

#
# def Nice_Date(df, dateformat):
#     for row in df:
#       row['year_week_formatted'] = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
#     result = a + b
#     return str(result)
#
# # print(df_country['year_week'].head())
# # df_country['Test_Weeks'] = df.apply(lambda x: my_function(x['value_1'], x['value_2']), axis=1)

# function to returns date
# def niceDate(year_week):
# 	return datetime.datetime.strptime(year_week + '-1', "%Y-W%W-%w")

d = "2013-W05"
a = nicedate(d)
# r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
print(a)
print(r)
#
# def format_date(df, dateformat):
#     """this will format the column containing dates'"""
#     for row in df:
#         row['Date'] = datetime.datetime.strptime(row['Date'], '%Y%m%d')
#         csv.DictWriter(str(df)+'_converted.csv', data)
#         return