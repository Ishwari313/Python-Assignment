import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

Border = "="*50

# Step 1: Load Dataset

print(Border)
print("Step 1 : Load Dataset")
print(Border)

df = pd.read_csv("School1.csv")

print("The few records from the dataset")
print(df.head())

# Step 2 : Check Missing values

print(Border)
print("Step 2:  check the missing values")
print(Border)

print("Missing values Count :\n",df.isnull().sum())

#Step 3: Display Statistical Summary

print(Border)
print("Step 3 : Display Statistical Summary")
print(Border)

print(df.describe())

# step 4 : Correlation between columns

print(Border)
print("Step 4 : Correlation between columns")
print(df.corr())

# step 5 : Split data into Independent and dependent Varibales
print(Border)
print("Step 5 : Split the datst into Independt and dependent varibales")
print(Border)


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)


print("X_train shape :",X_train.shape)
print("X_test shape:",X_test.shape)
print("Y_train shape :",Y_train.shape)
print("Y_test shape :",Y_test.shape)
