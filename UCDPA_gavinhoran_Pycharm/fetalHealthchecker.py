import pandas as pd

fetalHealth = pd.read_csv('fetal_health.csv')
print(fetalHealth.head())
print(fetalHealth.info())
print(fetalHealth['movement'])