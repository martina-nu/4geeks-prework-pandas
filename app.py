import pandas as pd

# IMPORT PANDAS
#data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(data_frame)

# SERIES
#ages = pd.Series([23,45,7,34,6,63,36,78,54,34])
#print(ages)

#SERIES DATE RANGE
#DatetimeIndex = pd.date_range("05-01-2021","05-12-2021")
#print(DatetimeIndex)

# SERIES APPLY
#my_series = pd.Series([2,4,6,8,10])

#def div(x):
   # return x/2

#print(my_series.apply(div))

# PANDAS DATA FRAME

#data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]

#df = pd.DataFrame(data,columns=["Brand","Model","Color"])

#print(df)

#PANDAS DF FROM DICTIONARY
"""
data = [
    { 
        "brand": "Toyota", 
        "make": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "make": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porche", 
        "make": "Cayenne",
        "color": "White"
    },
    {"brand": "Tesla",
    "make": "Model S",
    "color": "Red"
    
    }
]
"""

#df = pd.DataFrame(data)

#print(df)

#DATAFRAME ILOC

#data = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(data.iloc[133,6])


#File head and tail

#data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(data.head(3))
#print(data.tail(3))

#print(data_frame[['Name','Type 1']][0:10])

#print(data_frame.loc[data_frame['Attack']> 80])

#print(len(data_frame.loc[data_frame['Legendary'] == True]))

data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
#print(data_frame.head(5))

#data_frame = data_frame.drop('Unnamed: 0', axis=1)
#print(data_frame.head(5))

#count = data_frame['Gender'].value_counts()
#print(count)

names = data_frame.groupby("Name").sum()
print(len(names))
