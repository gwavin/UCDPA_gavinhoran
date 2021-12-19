# C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\UCDPA_gavinhoran_Pycharm\ECDCCovidTestingData.csv contains
# info about testing volume for COVID-19 by week and country.
# Each row contains the corresponding data for a country and a week. The file is updated weekly. You may use the data
# in line with ECDC’s copyright policy.
# Source: The figures displayed for weekly testing rate and weekly test positivity are based on multiple data sources.
# The main source is data submitted by Member States to the European Surveillance System (TESSy), however, when not
# available,
# ECDC compiles data from public online sources. EU/EEA Member States report in TESSy all tests performed (i.e. both
# PCR and antigen tests).
# The data displayed from public online sources have been automatically or manually
# retrieved (‘web-scraped’) on a daily basis. It should be noted that there are limitations to this
# type of data including that definitions vary and the data collection process requires constant adaptation to avoid
# to interrupted time series
# (i.e. due to modification of website pages, types of data).

# Import Matplotlib and Seaborn
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ECDCCovidTestingData.csv')
irishData = df[df['country_code']=='DE'] #Only looking at Irish data for now,removing other data I don't wiash to look
# at

# Create line plot

sns.lineplot(x="year_week",y="testing_rate",data=irishData)
# sns.relplot(x="year_week",y="positivity_rate", data=irishData, kind="line")


plt.xticks(rotation= 90)
# plt.plot()
# Show plot
plt.show()
# print(df['year_week'])


# Determine the date
#df1 = df("week_start", F.to_date(F.concat(F.col("year_week"), F.lit("-1")), "YYYY-'W'ww-u")).withColumn("week_end", F.next_day(F.col("week_start"), "SUN"))

# # Plot
# fig, ax = plt.subplots()
# df.plot(x='date', y='tests_done', marker='o', ax=ax)
#
# # Format the x-ticks
# myFmt = mdates.DateFormatter('%Y week %U')
# ax.xaxis.set_major_formatter(myFmt)
#

# for i in range(df['year_week'])
# def loop_impl(df):
#   TestDates = datetime.date.today() + datetime.timedelta(days=2)
#   result = []
#   for i in range(df([year_week]):
#     row = df.iloc[i]
#     result.append(
#       eisenhower_action(
#         r = datetime.datetime.strptime(d, "%Y-W%W")
#         row.priority == 'HIGH', row.due_date <= cutoff_date)
#     )
#   return pd.Series(result)
#
# import datetime
# d = "2013-W26"
# r = datetime.datetime.strptime(d, "%Y-W%W")
# print(r)