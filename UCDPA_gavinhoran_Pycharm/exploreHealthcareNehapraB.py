# import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

train_df = pd.read_csv('healthcare/train_data.csv')
test_df = pd.read_csv('healthcare/test_data.csv')

# print(train_df.head())
#
#
# for col in train_df.columns:
#     print(col)
#
# test_df.info()

#
# # visualize Length of Stay intervals only
# plt.figure.Figure(figsize = (15,10))
# sns.countplot(y = 'Stay', data = train_df, palette = 'Set3')
# plt.xlabel('Admissions', size = 25)
# plt.ylabel('Length of Stay (in days)', size = 25)
# plt.title('Number of Admissions per Length of Stay(n = {})'.format(len(train_data)))
# plt.show()

# visualize distribution of LOS by age cohort
los_indices = train_df.Stay.value_counts().index[:11]
age_indices = train_df.Age.value_counts().index[:10]
cross_data = train_df[train_df.Stay.isin(los_indices) & (train_df.Age.isin(age_indices))]
plt.figure()
# cross_table = pd.crosstab(columns=cross_data.Stay, index=cross_data.Age)
# cross_table.plot.bar(figsize=(10, 10), title="Stay Lengths per Age cohort")
# plt.xlabel('Age cohorts', size=20)
# plt.ylabel('Admissions', size=20)
plt.show()
