import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.cbook as cbook

#this data comes from ECDC testing data
#https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv

sns.set_style('darkgrid') # darkgrid, white grid, dark, white and ticks
plt.rc('axes', titlesize=12)     # fontsize of the axes title
plt.rc('axes', labelsize=4)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=9)    # fontsize of the tick labels
plt.rc('ytick', labelsize=9)    # fontsize of the tick labels
plt.rc('legend', fontsize=9)    # legend fontsize
plt.rc('font', size=13)          # controls default text sizes

df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')

country = ['IE', 'DE', 'ES', 'FR', 'NL']#looking at five comparable countries IE_DE_ES_FR_NL_Testing.py
df_country = df[df["country_code"].isin(country)]
# print(df_country['year_week'].head())
# df_country['Test_Weeks'] = df.apply(lambda x: my_function(x['value_1'], x['value_2']), axis=1)
def niceDate(year_week):
	return datetime.datetime.strptime(year_week + '-1', "%Y-W%W-%w")

df = df.copy()
df_country['Test_Dates'] = df['year_week'].apply(niceDate)

#print(df_country['Test_Dates'].head())


sns.lineplot(x="Test_Dates",y="testing_rate",data=df_country,hue='country_code')
plt.savefig('dateDefGraphs.png')
plt.show()



