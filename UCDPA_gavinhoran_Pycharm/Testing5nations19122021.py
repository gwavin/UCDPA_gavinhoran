import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.cbook as cbook

sns.set_style('darkgrid') # darkgrid, white grid, dark, white and ticks
plt.rc('axes', titlesize=12)     # fontsize of the axes title
plt.rc('axes', labelsize=10)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)    # fontsize of the tick labels
plt.rc('ytick', labelsize=10)    # fontsize of the tick labels
plt.rc('legend', fontsize=10)    # legend fontsize
plt.rc('font', size=13)          # controls default text sizes

#this data comes from ECDC testing data
#https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv

df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')

country = ['IE', 'DE', 'ES', 'FR', 'NL']#looking at five comparable countries IE_DE_ES_FR_NL_Testing.py
df_country = df[df["country_code"].isin(country)]
# print(df_country['year_week'].head())
# df_country['Test_Weeks'] = df.apply(lambda x: my_function(x['value_1'], x['value_2']), axis=1)
def niceDate(year_week):
	return datetime.datetime.strptime(year_week + '-1', "%Y-W%W-%w")

#df_country['Test_Dates'] = df['year_week'].apply(niceDate)

df_country = df_country.copy()
df_country['Test_Dates'] = df_country.iloc[:,2].apply(niceDate)


#df_country_name_index = df_country
#print(df_country['Test_Dates'].head())

# df_country_name_index.set_index("year_week")
#
# print(df_country_name_index.iloc[1000])
# print(df_country_name_index.head())

sns.lineplot(x="Test_Dates",y="testing_rate",data=df_country,hue='country_code')
plt.title("Testing in 5 European Nations")
plt.xticks(rotation= 45)
plt.show()





