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



import pandas as pd
df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')
df2 = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/virusvariant/csv/data.csv')
# This is a for loop!
# print("df")
# for col in df.columns:
#     print(col)
#
# print("df2")
# for col in df2.columns:
#     print(col)

df_new = pd.merge(df, df2, left_on=('country', 'country_code', 'year_week'),right_on=('country', 'country_code', 'year_week'), how="outer")
print(df_new.head())
df_new.to_csv(r'variantAndTestingDataMerged.csv')
for col in df_new.columns:
    print(col)

# country = ['IE', 'DE', 'ES', 'FR', 'NL']  # looking at five comparable countries IE_DE_ES_FR_NL_Testing.py
country = ['IE']  # looking at ireland only

# taking a subset of these countries, graph was too crowded otherwise.
df_country = df[df["country_code"].isin(country)]


def my_dater(year_week):
    return datetime.datetime.strptime(year_week + '-1', "%Y-W%W-%w")


df = df.copy()
df_country['TestingDates'] = df_country['year_week'].apply(my_dater)

# fig = plt.figure()
fig, axes = plt.subplots(figsize=(10, 6))

t1 = sns.lineplot(x="TestingDates", y="testing_rate", data=df_country, label="Testing Rate")  # first plot

t2 = sns.lineplot(x="TestingDates", y="new_cases", data=df_country,
                  label="Detection of New Cases")  # second plot i want these to share axes;

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
# plt.xticks(rotation=45)
plt.savefig('teSTINGvDetectionIreland.png')
plt.show()
