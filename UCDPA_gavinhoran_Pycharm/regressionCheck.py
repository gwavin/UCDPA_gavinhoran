import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.cbook as cbook
# this data comes from ECDC testing data
# https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv
sns.set_style('darkgrid')  # darkgrid, white grid, dark, white and ticks
plt.rc('axes', titlesize=12)  # fontsize of the axes title
plt.rc('axes', labelsize=10)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)  # fontsize of the tick labels
plt.rc('ytick', labelsize=10)  # fontsize of the tick labels
plt.rc('legend', fontsize=10)  # legend fontsize
plt.rc('font', size=13)  # controls default text sizes

df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')

#country = ['IE', 'DE', 'ES', 'FR', 'NL']  # looking at five comparable countries IE_DE_ES_FR_NL_Testing.py
country = ['IE']  # looking at ireland only

#taking a subset of these countries, graph was too crowded otherwise.
df_country = df[df["country_code"].isin(country)]


def my_dater(year_week):
    return datetime.datetime.strptime(year_week + '-1', "%Y-W%W-%w")

df = df.copy()
df_country['TestingDates'] = df_country['year_week'].apply(my_dater)

sns.regplot(data=df_country,
         y='tests_done',
         x="new_cases",
         marker='^',
         color='g',order=1)

# np.corrcoef(np_city[:,0], np_city[:,1])
# array([[ 1.     , -0.01802],       [-0.01803,  1.     ]])
# np.std(np_city[:,0])0.1992


plt.title("regression, order = 1")
plt.savefig('testingSaveRegressionOrder2.png')
plt.show()