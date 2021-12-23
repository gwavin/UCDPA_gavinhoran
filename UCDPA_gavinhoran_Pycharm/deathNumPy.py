import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

death = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/nationalcasedeath_eueea_daily_ei/csv/data.csv")

df = death.groupby('countryterritoryCode')
dfg = death.groupby(["countryterritoryCode"]).mean()
# print(dfg)

# print(type(dfg))

dfgsorted = dfg.sort_values(by=['deaths'])
# only interested in ireland
dfgsorted.to_excel("deathsGroupedSorted.xlsx")
# ax = dfgsorted.hist(column='deaths', grid=False, figsize=(8,10), color='#86bf91')
#
# plt.xlabel('countryterritoryCode',fontsize=15)
# plt.ylabel('deaths',fontsize=15)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.title('avgDailyDeaths',fontsize=15)
#
#
#
# plt.show()
moreDeathThanIreland = dfgsorted.index[dfgsorted['deaths'] > 19.65 ].tolist()
print(moreDeathThanIreland)
death_ireland = death[death['countryterritoryCode'] == 'IRL']
# print(np.mean(death_ireland['deaths']))


# print(death_ireland.head()) I was checking I had the right data.

# There are a lot of zero entries; I would like to remove those;

death_ireland = death_ireland.loc[death_ireland['deaths'] != 0]
# print(death_ireland.info)
# print(np.mean(death_ireland['deaths']))

