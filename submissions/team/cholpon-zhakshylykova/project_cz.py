# import the necessary libraries: 

import kagglehub
import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns

#------------ get the data -------------

# Download latest version
path = kagglehub.dataset_download("mrsimple07/energy-consumption-prediction")

print("Path to dataset files:", path)

#check the directory
print(os.listdir(path))

data = pd.read_csv(os.path.join(path, "Energy_consumption.csv"))

#------------EDA-------------------------
data.head(10)

#convert the "Timestamp" column to datetime
#The to_datetime() function is used to convert argument to datetime.

data["Timestamp"] = pd.to_datetime(data["Timestamp"])
data.describe()
data.info()
'''
DatetimeIndex: 1000 entries, 2022-01-01 00:00:00 to 2022-02-11 15:00:00
Data columns (total 10 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   Temperature        1000 non-null   float64
 1   Humidity           1000 non-null   float64
 2   SquareFootage      1000 non-null   float64
 3   Occupancy          1000 non-null   int64  
 4   HVACUsage          1000 non-null   object 
 5   LightingUsage      1000 non-null   object 
 6   RenewableEnergy    1000 non-null   float64
 7   DayOfWeek          1000 non-null   object 
 8   Holiday            1000 non-null   object 
 9   EnergyConsumption  1000 non-null   float64
dtypes: float64(5), int64(1), object(4)
'''

#set timestamp as index
data.set_index("Timestamp", inplace=True) #keep the indexed timestamp as a column

print(len(data.columns))
'''10 columns'''


#find the initial and the end date

print(f"Initial date: {data.index.min()}")
print(f"End date: {data.index.max()}")

#since the data is all synthetic it is okay to experiment with all the possible ways to analyze the data. 

data.head(10)
'''Same dates are asigned as a holiday and non-holiday, therefore I will drop the columns [Holiday] [DayOfWeek]'''

print(data.columns)
data.drop(["Holiday", "DayOfWeek"], axis = 1, inplace=True)
data.head()


#Outlier Detection with IQR:

Q1 = data["EnergyConsumption"].quantile(0.25)
print(f"Q1: {Q1}")

Q3 = data["EnergyConsumption"].quantile(0.75)
print(f"Q3: {Q3}")

IQR = Q3 - Q1
print(IQR)

lower_bound_outlier = Q1 - 1.5*IQR
upper_bound_outlier = Q3 + 1.5*IQR



#correlation analysis


