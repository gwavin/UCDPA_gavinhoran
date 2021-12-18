# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/csv/data.csv'
# Save file locally
urlretrieve(url,'data.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('data.csv', sep=';')
print(df.head())

pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('YearWeekISO (this thing)')
plt.ylabel('count')
plt.show()
