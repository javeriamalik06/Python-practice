# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:12:01 2024

@author: Javeria Malik
"""
import os
os.chdir('C:\\Javeria\\Projects\\Data Science Roadmap\\Numpy, pandas, matplotlib - Week 3\\Pandas, Matplotlib and Seaborn\\Video notes')
#PANDAS
import pandas as pd
df=pd.read_csv('movies.csv')
df
#print first 5 rows unless specified
df.head()
df.head(2)
#print random rows
df.sample(4)
#print rows 2 to 5
df[2:5]
#prints shape
df.shape
#calc avg imdb_rating
    #printing the column
df['imdb_rating']
#or
df.imdb_rating
#a column in df object is called series
#printing min max mean
df.imdb_rating.min(), df['imdb_rating'].max(), df.imdb_rating.mean()
#calculating only avg for hollywood or bollywood movie
    #applying filter on df
df_h=df[df.industry=='Hollywood']
df_b=df[df.industry=='Bollywood']
#printing min max mean for hollywood
df_h.imdb_rating.min(), df_h['imdb_rating'].max(), df_h.imdb_rating.mean()
#printing min max mean for bollywood
df_b.imdb_rating.min(), df_b['imdb_rating'].max(), df_b.imdb_rating.mean()

#DATAFRAME BASICS
#print columns
df.columns
#finding out unique industries
df.industry.unique()

df.language.unique()
#how many bollywood and hollywood movies are there
df.industry.value_counts()
df.language.value_counts()

#printing subset of df
df_new = df[['title','imdb_rating','industry']]
#printing movies from 2000 to 2010
df[(df.release_year>=2000) & (df.release_year<=2010)]
#finding unique studios to get marvel name
df.studio.unique()
#getting marvel movies
df[df.studio=="Marvel Studios"]

#quick stats overview
df.describe()
#shows null values data
df.info()
#printing max and min movie (| means or)
df[(df.imdb_rating==df.imdb_rating.max()) | (df.imdb_rating==df.imdb_rating.min())]

df.head()
#printing age of the movie
#lambda x is a quick way of writing python function. sort of like a for loop. for first row and then moving fwd
#in below formula x is release year
df['age'] = df['release_year'].apply(lambda x: 2023 - x)
df
#making a profit column
#we make the axis 1 because we need columns
df['profit']=df.apply(lambda x: x['revenue'] - x['budget'], axis=1)
#can also be written as
df['profit']=df['revenue']-df['budget']

df.head()

#index operation
df.index
#changing the index to the title column
#inplace has to be True to modify the original dataframe
df.set_index('title', inplace=True)
df.index
#it prints the whole info about the movie below
df.loc['Pather Panchali']
df.loc[['Pather Panchali','Thor: The Dark World ']]

#printing rows on integer based location
df.iloc[0]
df.iloc[2:6]

#resetting the index
df.reset_index(inplace=True)
df

#READ CSV FILE
import pandas as pd
df=pd.read_csv("stock_data.csv")
df=pd.read_csv("stock_data.csv", skiprows=1)
df
#or
df=pd.read_csv("stock_data.csv", header=1)
#changing the column names through read_csv
df=pd.read_csv("stock_data.csv", header=1, names=['stock symbol','eps','revenue','price','people'])
#to read only 4 rows
df=pd.read_csv("stock_data.csv", header=1, nrows=4)
df
#to input proper NA values instead of strings
df=pd.read_csv("stock_data.csv", header=1, na_values={
    'eps': ["not available"],
    'revenue': [-1],
    'people': ['n.a.']
})
df
#replacing all not available as na values
df=pd.read_csv("stock_data.csv", header=1, na_values=['not available','n.a.'])

#WRITING CSV
#creating a pe ratio column and then exporting
df['pe']=df['price']/df['eps']
df

#exporting a csv file
df.to_csv('pe_exported.csv')
#to remove index
df.to_csv('pe_exported.csv', index=False)
#to remove header
df.to_csv('pe_exported.csv', index=False, header=False)

#reading the excel
df_movies=pd.read_excel('movies_db.xlsx', 'movies')
df_financials=pd.read_excel('movies_db.xlsx', 'financials')

df_movies.head(4)
df_financials.head(4)

#to convert the Dollars and $$ to USD 
def standardize_currency(curr):
    if curr == 'Dollars' or curr == '$$':
        return 'USD'
    return curr

df_financials=pd.read_excel('movies_db.xlsx', 'financials', converters= {
    'currency': standardize_currency})

df_financials.head(4)

#joining the movies and financials data
df_merged=pd.merge(df_movies, df_financials, on='movie_id')
df_merged.head(4)
#exporting to excel
df_merged.to_excel('movies_merged_exported.xlsx', sheet_name='merged', index=False)

#adding two dfs to the same excel as different sheets
df_stocks=pd.DataFrame({
    'tickers':['GOOG','WMT','MSFT'],
    'price':[845,65,64],
    'pe':[30.37,14.26,30.97]
    })
df_stocks

df_weather=pd.DataFrame({
    'day':['2017/1/1','2015/5/6'],
    'temperature':[32,35],
    'event':['Rain','Snow']})

with pd.ExcelWriter("stocks_weather_exported.xlsx") as writer:
    df_stocks.to_excel(writer, sheet_name='stocks', index=False)
    df_weather.to_excel(writer, sheet_name='weather', index=False)

#HANDLE NA VALUES
#the day data is strings, hence to convert into date
df=pd.read_csv('weather_data.csv', parse_dates=['day'])

type(df.day[0])

df.set_index('day', inplace=True)
#replacing NA values with 0
df.fillna(0)
#replacing NA values with mean values
df.temperature.mean()
df.fillna({
    'temperature':df.temperature.mean(),
    'windspeed':df.windspeed.mean(),
    'event':'No event'})
#replacing NA with peechay wali value (forward fill)
df.fillna(method='ffill')
#replacing NA with agay wali value (backward fill)
df.fillna(method='bfill')
#replacing NA with agay wali value on the right column (backward fill)
df.fillna(method='bfill', axis='columns')
#replacing NA with peechay wali value (forward fill) and limit to only 1 replacement
df.fillna(method='ffill', limit=1)
#to linearly fill the NA values (32 and 28 k beech me 30)
df.interpolate()
#Drop NA values
df.dropna()
#how to drop it
#if all data values are NA then drop it
df.dropna(how='all')
#specifying threshold
#atleast 2 Non NA values should be there
df.dropna(thresh=2)

#Importing another weather data file
df=pd.read_csv('weather_data_2.csv')
df

#-99999 means null values
#to replace with zero
df.replace(-99999,0)

#to replace -99999 as NaN
import numpy as np
df.replace(-99999,np.nan)

df.replace([-99999,-88888],np.nan)
#can also be written as
df.replace(to_replace=[-99999,-88888],value=np.nan)
#replacing different values per column
df.replace({
    'temperature':-99999,
    'windspeed': [-99999,-88888],
    'event':'no event'}, np.nan)
#replacing values per the replaced values for all columns
df.replace({
    -99999:np.nan,
    -88888:np.nan,
    'no event':'Sunny'})

#creating a new df
df=pd.DataFrame({
    'score':['exceptional','average','good','poor','average','exceptional'],
    'student':['Javeria','Ahmed','Ayesha','Ayeza','Shiza','Appiya']})
#replacing the words with numerical grade
df.replace(['poor','average','good','exceptional'],[1,2,3,4])
#replacing only in the student column
df['student'].replace({'Ayesha':'bby','Shiza':'Theedo','Ayeza':'Ayedo'}, inplace=True)
df

#GROUP BY 
df=pd.read_csv('weather_by_cities.csv')
df
#random filtering
df[df.event=='Rain'].temperature.mean()
#filtering the dataframe per city
df[df.city=='new york'].temperature.max()
#using group by instead
#the below returns the object that enables groupby
g=df.groupby('city')

for city, data in g:
    print('city:',city)
    print('\n')
    print('data:',data)
#so to find out max temps by cities we do this
for city, data in g:
    print('city:',city)
    print('\n')
    print('max:',data.temperature.max())

#to get specific group(city) data
g.get_group('mumbai')

#g.max returns max for all columns and all cities. for event alphabetical max
g.max()
#mean for all
g[['temperature','windspeed']].mean()
g.min()
#quick statistics
g.describe()
#size of df
g.size()

#making groups of temperatures
def grouper(df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return '80-90'
    elif 50 <= df[col].loc[idx] <= 60:
        return '50-60'
    else:
        return 'others'
#defining groupby g
g = df.groupby(lambda idx: grouper(df, idx, 'temperature'))

#all values in groups
for key, data in g:
    print('key:',key)
    print('data:',data)

g[['temperature','windspeed']].mean()

g.max()

#CONCAT AND MERGE

india_weather=pd.DataFrame({
    'city':['mumbai','delhi','bangalore'],
    'temperature':[32,45,30],
    'humidity':[80,60,78]})

us_weather=pd.DataFrame({
    'city':['new york','chicago','orlando'],
    'temperature':[21,14,35],
    'humidity':[68,65,75]})

#stacking the dfs on top
df=pd.concat([india_weather,us_weather])
#ignoring index
df=pd.concat([india_weather,us_weather], ignore_index=True)
#specifying keys
df=pd.concat([india_weather,us_weather], keys=['india','us'])
#selecting index 1 from india
df.loc['india'].iloc[1]

temperature_df=pd.DataFrame({
    'city':['mumbai','delhi','bangalore'],
    'temperature':[32,45,30]}, index=[0,1,2])

windspeed_df=pd.DataFrame({
    'city':['delhi','mumbai'],
    'windspeed':[7,12]}, index=[1,0])

#axis 1 to concat on columns
pd.concat([temperature_df,windspeed_df], axis=1)
#to merge these
#default join is inner hence bangalore doesnt show
pd.merge(temperature_df,windspeed_df,on='city')
#to see bangalore we have to do left join
pd.merge(temperature_df,windspeed_df,on='city', how='left')
#same can be done with right join
#outer join returns all from both dfs


#MATPLOTLIB AND SEABORN IN JUPYTER
























