# 2. Display the first 5 records of the dataset

import pandas as pd

Border = "-"*50

print(Border)
print("Step 1: Load the dataset ")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print("Dataset gets loaded Successfully....")

print("Initial Entries from the dataset :")
print(df.head())

print("Last 5 entries from the dataset:")
print(df.tail())

print()

print("Totl number of rows is :",df.shape[0])
print("Totl number of columns is :",df.shape[1])

print()

print("Column from dataset is :",df.columns)

print()

print("Datatype of each column is :")
print(df.dtypes)

print()

print("Total no of student from dataset is :",df.shape[0])

print()

passed_count = df["FinalResult"].sum()

print("Number of students passed:",passed_count)

print()


failed_count =(df["FinalResult"]==0).sum()

print("Number of students failed:",failed_count)