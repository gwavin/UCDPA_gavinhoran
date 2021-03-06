import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import pandas as pd

# this data comes from ECDC testing data
# https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv
from UCDPA_gavinhoran_Pycharm.functionFile import my_dater
from UCDPA_gavinhoran_Pycharm.functionFile import png_time_namer

sns.set_style('darkgrid')  # darkgrid, white grid, dark, white and ticks
plt.rc('axes', titlesize=12)  # fontsize of the axes title
plt.rc('axes', labelsize=10)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)  # fontsize of the tick labels
plt.rc('ytick', labelsize=10)  # fontsize of the tick labels
plt.rc('legend', fontsize=10)  # legend fontsize
plt.rc('font', size=13)  # controls default text sizes

df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')

# country = ['IE', 'DE', 'ES', 'FR', 'NL']  # looking at five comparable countries IE_DE_ES_FR_NL_Testing.py
country = ['NL']  # looking at ireland only, because when I looked at the rest it was really messy and any connection
# between the data and the plot was lost. One country at a time was good. I suppose this would be a good time to
# explain why I think that;s the case. In Ireland, the number of tests done at the start was linked quite well with
# how many # new cases there might be. We were ramping up our capacity to test. As a result the number of people
# being tested was limited not by the necessity but by the numbers. As time goes by, the capacity for testing goes
# up, and this means that we are more capable of picking out peaks and troughs; previously, we were detecting as much
# as we could; the likely number of new cases was highly bound to the number of tests. Now we have loads of tests. So
# if there are more available tests, we can generate a more accurate picture of what is happening, with less
# dependence on the number of tests we actually are capable of doing.

# taking a subset of these countries, graph was too crowded otherwise.
df_country = df[df["country_code"].isin(country)]

#
# def my_dater(year_week):
#     return datetime.datetime.strptime(year_week + '-1', "%Y-W%W-%w")

df = df.copy()
df_country['TestingDates'] = df_country['year_week'].apply(my_dater)

sns.lmplot(data=df_country,
           x='tests_done',
           y="new_cases",
           order=2)


# decided to make new cases dependent because you can't really get new case numbers without doing tests.
plt.title("lmplot,Tests_done (independent )v. new cases(dependent), Order = 2")


print(str(datetime.datetime.now()))
t='{0:%H%M%S%d%m%y}'.format(datetime.datetime.now())
print(t)

filename = 'lmplotTestsV'



plt.savefig(png_time_namer(filename))
plt.show()


date = datetime.datetime.now().strftime("%I%M%S%d%m%Y")
print(f"filename_{date}")
#
# def time_namer(date):
#       shite one: return datetime.datetime.now().strftime(date, "%I%M%S%d%m%Y")
#     return datetime.datetime.strptime(date + '-1', "%Y-W%W-%w")

