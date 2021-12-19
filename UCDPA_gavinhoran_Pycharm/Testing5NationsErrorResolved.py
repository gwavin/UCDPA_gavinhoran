import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.cbook as cbook

sns.set_style('darkgrid')  # darkgrid, white grid, dark, white and ticks
plt.rc('axes', titlesize=12)  # fontsize of the axes title
plt.rc('axes', labelsize=10)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)  # fontsize of the tick labels
plt.rc('ytick', labelsize=10)  # fontsize of the tick labels
plt.rc('legend', fontsize=10)  # legend fontsize
plt.rc('font', size=13)  # controls default text sizes

# this data comes from ECDC testing data
# https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv

df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')

country = ['IE', 'DE', 'ES', 'FR', 'NL']  # looking at five comparable countries IE_DE_ES_FR_NL_Testing.py
df_country = df[df["country_code"].isin(country)]


def my_dater(year_week):
    return datetime.datetime.strptime(year_week + '-1', "%Y-W%W-%w")

df = df.copy()
df_country['TestingDates'] = df_country['year_week']
df_country['TestingDates'] = df_country['TestingDates'].apply(my_dater)

sns.lineplot(x="TestingDates", y="testing_rate", data=df_country, hue='country_code')
plt.title("Testing in 5 European Nations")
plt.xticks(rotation=45)
plt.show()
