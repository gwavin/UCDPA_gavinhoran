from datetime import date, timedelta
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.cbook as cbook
# this data comes from ECDC testing data
# https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv
from UCDPA_gavinhoran_Pycharm.functionFile import my_dater

sns.set_style('darkgrid')  # darkgrid, white grid, dark, white and ticks
plt.rc('axes', titlesize=12)  # fontsize of the axes title
plt.rc('axes', labelsize=10)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)  # fontsize of the tick labels
plt.rc('ytick', labelsize=10)  # fontsize of the tick labels
plt.rc('legend', fontsize=10)  # legend fontsize
plt.rc('font', size=13)  # controls default text sizes

df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')

# country = ['IE', 'DE', 'ES', 'FR', 'NL']  # looking at five comparable countries IE_DE_ES_FR_NL_Testing.py
country = ['IE']  # looking at ireland only

#taking a subset of these countries, graph was too crowded otherwise.
df_country = df[df["country_code"].isin(country)]




df = df.copy()
df_country['TestingDates'] = df_country['year_week'].apply(my_dater)
df_sixmonths = df_country.copy()
df_sixmonths = df_sixmonths[(df_sixmonths['TestingDates'].dt.year == 2021)]#use of a boolean here; also subsetting
#| (df_sixmonths['TestingDates'] >= )

#fig = plt.figure()
fig, axes = plt.subplots(figsize=(10, 6))

t1 = sns.lineplot(x="TestingDates", y="testing_rate", data=df_sixmonths,label="Testing Rate",hue='country_code')  # first plot

t2 = sns.lineplot(x="TestingDates", y="new_cases", data=df_sixmonths,label="Detection of New Cases",hue='country_code')  # second plot i want these to share axes;

# the first subplot
ax0 = plt.subplot(t1)
# the second subplot
# shared axis X
ax0.set_ylabel('Cases', color='g')

ax1 = plt.subplot(t2, sharex=ax0)
ax1.set_ylabel('Testing', color='b')

# remove vertical gap between subplots
plt.subplots_adjust(hspace=.0)
plt.title("Testing and new cases in Ireland")
#plt.xticks(rotation=45)
plt.savefig('teSTINGvDetectionIreland.png')
plt.show()
