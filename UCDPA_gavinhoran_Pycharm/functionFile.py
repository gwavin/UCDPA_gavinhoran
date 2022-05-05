import matplotlib.pyplot as plt
import datetime
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
def niceDate(year_week):
    return datetime.datetime.strptime(year_week + '-1', "%Y-W%W-%w")


# Below was how I made the bit above. d is an example of what a date looked like in the ECDC data; then I run
# niceDate on it. technically, it shouldn't have any uppercase in it, I know that now. I have an overconversational style of 
# commenting. But I think it makes my code more readable. 
d = "2013-W05"
a = niceDate(d)
r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")


# I am not sure why I commented this out. I think I may have redefined it within the text of another .py file, and so there may have been a conflict. 
# My programming discipline was not tight. 
# def format_date(df, dateformat):
#     """this will format the column containing dates'"""
#     for row in df:
#         row['Date'] = datetime.datetime.strptime(row['Date'], '%Y%m%d')
#         csv.DictWriter(str(df)+'_converted.csv', data)
#         return

# I made this to take a given filename, which I've imaginatively called filename, and to append the time and date to it, in the format
# HHMMSSDDMMYY and then to place that in front of ".png".... Okay, I'm going to do something crazy.
#
def png_time_namer(filename):
    t = '{0:%H%M%S%d%m%y}'.format(datetime.datetime.now())
    a = '.png'
    return (filename + t + a) # This was not a rude joke. 


def my_dater(year_week):
    return datetime.datetime.strptime(year_week + '-1', "%Y-W%W-%w")


def csv_time_namer(filename):
    t = '{0:%H%M%S%d%m%y}'.format(datetime.datetime.now())
    b = '.csv'
    return (filename + t + b)
