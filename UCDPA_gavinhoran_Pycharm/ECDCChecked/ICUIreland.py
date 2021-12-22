# This program demonstrates the use of a defined function; which is in functionfile; actually two of them;
# The use of the pandas, seaborn and matplotlib package.
# the import of a .csv; actually three of them
# the use of all of style adjustment on the graph
# the output of the merged .csv as a named file, using a function which I wrote;

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# from UCDPA_gavinhoran_Pycharm.FromJan2021 import my_dater
from UCDPA_gavinhoran_Pycharm.functionFile import png_time_namer, my_dater, csv_time_namer

# this data comes from ECDC testing data
# https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv
# These are two functions which I have tried to import.

# These are the various options available for the sns style list.
sns.set_style('darkgrid')  # darkgrid, white grid, dark, white and ticks
plt.rc('axes', titlesize=12)  # fontsize of the axes title
plt.rc('axes', labelsize=10)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)  # fontsize of the tick labels
plt.rc('ytick', labelsize=10)  # fontsize of the tick labels
plt.rc('legend', fontsize=10)  # legend fontsize
plt.rc('font', size=13)  # controls default text sizes

# this is the dataset from whence I have drawn most of my analysis
# df: Union[Union[TextFileReader, Series, DataFrame, None], Any] = pd.read_csv(
#     'https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')
df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')
df2 = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/virusvariant/csv/data.csv')
df3 = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/hospitalicuadmissionrates/csv/data.csv')

# This is merging; I just wanted to demo it; I'm going to use this for plots also;
df_new = pd.merge(df, df2, left_on=('country', 'country_code', 'year_week'),
                  right_on=('country', 'country_code', 'year_week'), how="outer")
df_newer = pd.merge(df3, df_new, left_on=('country', 'year_week'), right_on=('country', 'year_week'), how="outer")
# print(df_newer.head())
# plt.savefig(png_time_namer(filename))
df_Ire = df_newer[(df_newer['country']=='Ireland')]
df_Ire_ICU = df_Ire.query('indicator == "Daily ICU occupancy"')
df_sort_by_ICU = df_Ire_ICU

df_sort_by_ICU = df_sort_by_ICU.nlargest(20, 'value')
df_sort_by_ICU.to_csv("twentyWorstDays.csv")


# df_Ire_ICU = df_Ire_ICU.copy()
# df_Ire_ICU['date'] = pd.to_datetime(df_Ire_ICU['date'], format = '%Y-%m-%d')
# # df_country = df[df["country_code"].isin(country)]
# # print(df_Ire_ICU.head())
# # df_newer.to_csv(csv_time_namer('testVarHospMerger'))
#
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.lineplot(data=df_sort_by_ICU, x='date', y='value').set_title("COVID ICU Occupancy at worst")
next(df_sort_by_ICU.iterrows())
for index, value in df_sort_by_ICU.head(n=2).iterrows():
     print(index, row)
# #
# #
# # # counted_df = licenses_owners.groupby('title').agg({'account':'count'})
# # # filename = input('Please input the Filename and desired title for your plot: ')
# filename = 'COVID_ie_ICU'
# plt.savefig(png_time_namer(filename))
plt.show()
#
# #
# # # country = ['IE', 'DE', 'ES', 'FR', 'NL']  # looking at five comparable countries IE_DE_ES_FR_NL_Testing.py
# # country = ['IE']  # looking at ireland only, because when I looked at the rest it was really messy and any connection
# # # between the data and the plot was lost. One country at a time was good. I suppose this would be a good time to
# # # explain why I think that;s the case. In Ireland, the number of tests done at the start was linked quite well with
# # # how many # new cases there might be. We were ramping up our capacity to test. As a result the number of people
# # # being tested was limited not by the necessity but by the numbers. As time goes by, the capacity for testing goes
# # # up, and this means that we are more capable of picking out peaks and troughs; previously, we were detecting as much
# # # as we could; the likely number of new cases was highly bound to the number of tests. Now we have loads of tests. So
# # # if there are more available tests, we can generate a more accurate picture of what is happening, with less
# # # dependence on the number of tests we actually are capable of doing.
# #
# # # taking a subset of these countries, graph was too crowded otherwise; I am varying between Ireland by itself and the
# # # other five countries in the list
# # df_country = df[df["country_code"].isin(country)]
# #
# # # It took around an hour to figure out a way to make an error stop." value is trying to be set on a copy of a slice
# # # from a DataFrame." The slice below was being performed on a copy. From what I can tell, this creates a copy of the
# # # dataframe, the value is being set on a  copy of a dataframe which is not connected to the original, in terms of
# # # memory, and so the problem does not emerge
# # df = df.copy()
# # df_country['TestingDates'] = df_country['year_week'].apply(my_dater)
# #
# # # Finally, this makes the plot. Interestingly this comes second; I would guess that python goes all the way through
# # # the program and then goes back up, generating plots as it goes.
# # # I tested this by moving it to the bottom.... And it still didn't come first, and it lost it's data! I now think that...
# #
# #
# # # decided to make new cases dependent because you can't really get new case numbers without doing tests.
# # # plt.title("lmplot,Tests_done (independent )v. new cases(dependent), Order = 2")
# #
# # sns.lmplot(data=df_country,
# #            x='tests_done',
# #            y="new_cases",
# #            order=2)
# #
# # # file_name = 'mycsvfile' + str(datetime.now()) + '.csv'
# # # print(str(datetime.datetime.now()))
# # # t = '{0:%H%M%S%d%m%y}'.format(datetime.datetime.now())
# #
# # filename = input('Please input the Filename and desired title for your plot: ')
# # # plt.savefig('lmplotTestsVnew'+ t + '.png')
# #
# # # This line saves the fig
# # plt.title(filename)
# # plt.savefig(png_time_namer(filename))
# # plt.show()
# #
# # # This was just getting times out.
# # # date = datetime.datetime.now().strftime("%I%M%S%d%m%Y")
# # # print(f"filename_{date}")
