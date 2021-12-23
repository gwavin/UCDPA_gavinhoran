# This was pretty much solely to demonstrate the use of concat, to vertically merge the two datasets,
# and then drop_duplicates to bring it back down to the original. As noted in my implementation, the way that the
# ECDC stewarded their data meant that there were very few duplicated rows. Once the dataframes were carefully
# merged, across all columns they have in common, dropping duplicates was not necessary. Confirmed with Cian that
# demonstrating capacity was sufficient rather than including an example of the drop in the actual analysis.
#
import pandas as pd

df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')
print(df.shape)
df2 = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv')
print(df2.shape)


df_new = pd.concat([df, df2])
print(df_new.shape)
# print(df_new.head())

# for col in df_new.columns:
#     print(col)

# df_dropper = df_new.copy(deep=True)
df_new = df_new.drop_duplicates()
# print(df_new.head())
# for col in df_new.columns:
#     print(col)
print(df_new.shape)