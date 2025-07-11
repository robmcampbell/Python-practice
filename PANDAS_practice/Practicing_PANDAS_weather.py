import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('uk_weather.csv')

#Stating the cities being compared
cities = data['Location'].unique()
print("This dataset compares the temperature in the following cities:", cities)
print()

#finding the average temperature across all three cities
avg_temp = round(10*data['AvgTemp'].mean())/10
print(f"Average temperature across all cities: {avg_temp} °C")
print()

#finding the average temperature across each city
avg_temp_cities = data.groupby("Location")["AvgTemp"].mean()
print("Average temperature in each city in °C")
print(avg_temp_cities)
print()

#counting how many entries for each city
no_of_cities = data.groupby("Location")["AvgTemp"].count()
print("Number of entries for each city")
print(no_of_cities)

