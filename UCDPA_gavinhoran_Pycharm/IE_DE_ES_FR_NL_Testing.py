import matplotlib.pyplot as plt
from nicedate import nicedate
import seaborn as sns
import pandas as pd
import urllib.request
import urllib.request as tr


sns.set_style('darkgrid')  # darkgrid, white grid, dark, white and ticks
plt.rc('axes', titlesize=12)  # fontsize of the axes title
plt.rc('axes', labelsize=4)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=9)  # fontsize of the tick labels
plt.rc('ytick', labelsize=9)  # fontsize of the tick labels
plt.rc('legend', fontsize=9)  # legend fontsize
plt.rc('font', size=13)  # controls default text sizes

# this data comes from ECDC testing data
# https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv
#######
# Have to import the below url from webscraping
# #
# # Assign url of file: url
url = 'https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv'
# # Save file locally
urllib.request.urlretrieve(url, 'data.csv')
# # Read file into a DataFrame and print its head
df = pd.read_csv('data.csv', sep=';')
# print(df.head())
#############
# df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')
print(df.head())
country = ['IE', 'DE', 'ES', 'FR', 'NL']  # looking at five comparable countries IE_DE_ES_FR_NL_Testing.py
df_country = df[df["country_code"].isin(country)]
# df_country = df[df[‘nationality’].isin(country)]
df_country = df_country.copy()
print(df_country.iloc[:, 2].head())
df_country['year_week'] = df_country.iloc[:, 2].apply(nicedate)
# df_country = df_country['year_week'].apply(nicedate)
sns.lineplot(x="year_week", y="testing_rate", data=df_country, hue='country_code')
plt.show()
