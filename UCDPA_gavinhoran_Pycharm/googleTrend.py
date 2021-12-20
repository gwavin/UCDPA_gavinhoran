#All of the below code was modified from: https://towardsdatascience.com/a-very-precise-fast-way-to-pull-google-trends-data-automatically-4c3c431960aa

import seaborn as sns
import pandas as pd
import pytrends
from pytrends.request import TrendReq
pytrend = TrendReq()
import datetime as dt

# KEYWORDS=['Bitcoin','Ethereum','COVID-19','Trump']


KEYWORDS=['Bitcoin']

KEYWORDS_CODES=[pytrend.suggestions(keyword=i)[0] for i in KEYWORDS]
df_CODES= pd.DataFrame(KEYWORDS_CODES)
print(df_CODES.head())

EXACT_KEYWORDS=df_CODES['mid'].to_list()
DATE_INTERVAL='2016-01-01 2020-05-01'
COUNTRY=["US","GB","DE"] #Use this link for iso country code
CATEGORY=0 # Use this link to select categories
SEARCH_TYPE='' #default is 'web searches',others include 'images','news','youtube','froogle' (google shopping)

Individual_EXACT_KEYWORD = list(zip(*[iter(EXACT_KEYWORDS)]*1))
Individual_EXACT_KEYWORD = [list(x) for x in Individual_EXACT_KEYWORD]
dicti = {}
i = 1
for Country in COUNTRY:
    for keyword in Individual_EXACT_KEYWORD:
        print(keyword)
        pytrend.build_payload(kw_list=keyword,
                              timeframe = DATE_INTERVAL,
                              geo = Country,
                              cat=CATEGORY,
                              gprop=SEARCH_TYPE)
        dicti[i] = pytrend.interest_over_time()
        i+=1
df_trends = pd.concat(dicti, axis=1)


df_trends.columns = df_trends.columns.droplevel(0) #drop outside header
df_trends = df_trends.drop('isPartial', axis = 1) #drop "isPartial"
df_trends.reset_index(level=0,inplace=True) #reset_index
# df_trends.columns=['date','Bitcoin-US','Ethereum-US','COVID-19-US','Trump-US','Bitcoin-UK','Ethereum-UK','COVID-19-UK','Trump-UK','Bitcoin-Germany','Ethereum-Germany','COVID-19-Germany','Trump-Germany'] #change column names
print(df_trends.head())
# df_trends.columns=['date','Bitcoin-US'] #change column names
# #
# sns.set(color_codes=True)
# dx = df_trends.plot(figsize = (12,8),x="date", y=['Bitcoin-US','Bitcoin-UK','Bitcoin-Germany'], kind="line", title = "Bitcoin Google Trends")
# dx.set_xlabel('Date')
# dx.set_ylabel('Trends Index')
# dx.tick_params(axis='both', which='both', labelsize=10)