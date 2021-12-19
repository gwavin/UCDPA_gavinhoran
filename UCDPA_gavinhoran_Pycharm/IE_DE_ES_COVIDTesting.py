import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#this data comes from ECDC testing data

df = pd.read_csv('ECDCCovidTestingData.csv')
irishData = df[df['country_code']=='IE'] #Only looking at Irish data for now,removing other data I don't wiash to look
GermanData = df[df['country_code']=='DE']
SpanishData = df[df['country_code']=='ES']

sns.lineplot(x="year_week",y="testing_rate",data=irishData)
sns.lineplot(x="year_week",y="testing_rate",data=GermanData)
sns.lineplot(x="year_week",y="testing_rate",data=SpanishData)
# DE,FI,FR,IE,NL,SE
plt.title("Rate of Testing ")
plt.xticks(rotation= 90)
plt.xlabel("Weeks")
plt.ylabel("Rate of Testing")

# plt.plot()
# Show plot
plt.show()