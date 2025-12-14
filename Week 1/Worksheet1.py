"""
@author: Peyton Hall
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
In Class Coding:
"""

data1=pd.Series([1,3,5,7,9])
#print(data1)

databc = pd.read_excel(r'/Users/peytonhall/Desktop/DATA 499//Week 1/BreastCancer.xlsx')
#print(databc[2:5])

datafm1 = pd.DataFrame({"Name":["Tom", "Kate", "Mary"], "Age":[50,37,28], "Gender":["Male","Female","Female"]})
#print(datafm1)
datafm2 = pd.DataFrame({"Name":["Jack","Jerry"], "Age":[21,46], "Gender":["Male","Male"]})
#print(datafm2)
datafm3 = pd.concat([datafm1, datafm2], ignore_index = True)
#print(datafm3[2:4])

datacd = pd.read_excel(r'/Users/peytonhall/Desktop/DATA 499/Week 1/CARS.xlsx')
#print(datacd)

CARS = pd.read_excel("CARS.xlsx")
#print(CARS)
CARS1 = CARS[CARS.SIZE == "Small"]
#print(CARS1)
CARS2 = CARS[(CARS.SIZE=="Small")|(CARS.SIZE=="Large")]
#print(CARS2)

#print(SBPdata[SBPdata.Gender=="Female"])

CARwt = CARS.groupby("SIZE")["WEIGHT"].mean()
#print(CARwt)

CAR3 = CARS.drop(columns = ["CAR"])
CARave = CAR3.groupby('SIZE').mean()
#print(CARave)

#SBPave = SBPdata.groupby(['Member', 'Gender']).mean()
#print(SBPave)

#print(datafm3)
datafm3.columns = ["NAME", "AGE", "SEX"]
print(datafm3)

#SBPdata.columns = ['Membership', 'AGE', 'Blood pressure', 'SEX']

#SBPdata['BDP'] = [65, 79, 91, 80, 86, 77, 69, 92]
#print(SBPdata)

"""
Worksheet Questions:
"""

# 1) Create the data frame
df_members = pd.DataFrame({
	"Member": ["Yes","Yes","Yes","Yes","No","No","No","No"],
	"Age":    [25,35,40,50,75,40,60,65],
	"SBP":    [98,100,110,120,135,110,125,130],
	"Gender": ["Male","Female","Male","Female","Male","Female","Male","Female"]
})
print("1) Members dataframe:")
print(df_members)

# 2) Read the data CARS in Python and show the column of HIGHW
cars = pd.read_excel(r'/Users/peytonhall/Desktop/DATA 499/Week 1/CARS.xlsx')
print("\n2) HIGHWAY column:")
print(cars["HIGHWAY"].head())

# 3) Use the CARS data, print small cars and large cars using filter.
# Change 'SIZE' to match file
small_cars = cars[cars["SIZE"].str.lower() == "small"]
large_cars = cars[cars["SIZE"].str.lower() == "large"]
print("\n3) Small cars:")
print(small_cars.head())
print("\n3) Large cars:")
print(large_cars.head())

# 4) Use the CARS data, find the mean weight of each size of car.
mean_weight_by_size = cars.groupby("SIZE")["WEIGHT"].mean()
print("\n4) Mean WEIGHT by SIZE:")
print(mean_weight_by_size)

# 5) Use the CARS data, add the column of cylinder
if "CYLINDERS" in cars.columns:
    cars["CYLINDERS"] = cars["CYLINDERS"] # ensures it's present
else: # creates a placeholder
    cars["CYLINDERS"] = np.nan # or some rule to compute it if instructed
print("\n5) Added/confirmed CYLINDERS column:")
print(cars[["CAR","CYLINDERS"]].head())

# 6) Correct HIGHWAY by adding 10 to all original values
cars["HIGHWAY"] = cars["HIGHWAY"] + 10
print("\n6) HIGHWAY after +10 correction:")
print(cars["HIGHWAY"].head())

# 7) Replace values of CAR with only the model name (word before the first space)
cars["CAR"] = cars["CAR"].str.split().str[0]
print("\n7) CAR after keeping only first word:")
print(cars["CAR"].head())

# 8) Histogram of WEIGHT with 5 bins; comment out plt.show() if running headless
cars["WEIGHT"].plot(kind = "hist", bins = 5, edgecolor = "black", title = "WEIGHT distribution (5 bins)")
plt.xlabel("WEIGHT")
plt.ylabel("Count")
plt.show()