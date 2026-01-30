import pandas as pd
import numpy as np

## series in pandas is just a column of data
## dataframes is a collection of rows and columns

nums = [1,2,3,4,5]
series = pd.Series(nums)
print(series)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1,2,3])
print(fruits)

dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
series = pd.Series(dct)
print(series)

## Creating DataFrames from List of Lists
data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names', 'Country', "City"])
print(df)

## Creating DataFrame Using Dictionary
data = {'Name': ['Mide', 'Sofek', 'TunedIn'], 'Country': [
    'Nigeria', 'UK', 'Sweden'
], 'City': ['Lagos', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv('weight-height.csv')
print(df)

print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method
print(df.tail(2)) # tails give the last five rows, we can increase the rows by passing argument to tail method
print(df.shape) # as you can see 10000 rows and three columns

print(df.columns)

heights = df['Height'] # this is now a series
print(heights)

weights = df['Weight'] # this is now a series
print(weights)