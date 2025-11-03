import pandas as pd 
import matplotlib.pyplot as plt 

# CSV-Datei für Rotwein einlesen
df = pd.read_csv('/Users/carlplacek/Desktop/Uni/DataScience&KI/wine+quality/winequality-red.csv', sep=';')

print(df.head(6))
print(df.describe())