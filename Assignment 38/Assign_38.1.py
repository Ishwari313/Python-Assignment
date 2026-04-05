# 1. Write python program to load the file
# "Student_performannce_ml.csv" using pandas

import pandas as pd

print("Step 1: Load the dataset ")

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print("Dataset gets loaded Successfully....")