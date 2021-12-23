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

# Import Matplotlib and Seaborn#this worked so don't lose it.
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from UCDPA_gavinhoran_Pycharm.functionFile import my_dater
plt.rc('legend', fontsize=10)  # legend fontsize
df = pd.read_csv('ECDCCovidTestingData.csv')

df = df.copy()
df['TestingDates'] = df['year_week'].apply(my_dater)


irishData = df[df['country_code']=='IE'] #Only looking at Irish data for now,removing other data I don't wiash to look
GermanData = df[df['country_code']=='DE']
SpanishData = df[df['country_code']=='ES']


sns.lineplot(x="TestingDates",y="testing_rate",data=irishData,color='g')
sns.lineplot(x="TestingDates",y="testing_rate",data=GermanData,color='r')
sns.lineplot(x="TestingDates",y="testing_rate",data=SpanishData,color='b')


plt.xticks(rotation= 30)

# plt.plot()
# Show plot
plt.show()