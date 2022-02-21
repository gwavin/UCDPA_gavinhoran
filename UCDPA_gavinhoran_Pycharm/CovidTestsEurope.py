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

# df = pd.read_csv('ECDCCovidTestingData.csv')
# https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv
df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')
irishData = df[df['country_code']=='IE'] #Only looking at Irish data for now,removing other data I don't wiash to look
GermanData = df[df['country_code']=='DE']
SpanishData = df[df['country_code']=='ES']
NLData = df[df['country_code']=='NL']
sns.lineplot(x="year_week",y="testing_rate",data=irishData)
# sns.lineplot(x="year_week",y="testing_rate",data=GermanData)
# sns.lineplot(x="year_week",y="testing_rate",data=SpanishData)
sns.lineplot(x="year_week",y="testing_rate",data=NLData)



plt.xticks(rotation= 90)

# plt.plot()
# Show plot
plt.show()