# -----------------------------------------------
# 1. Load and Explore Dataset
# -----------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bank-full.csv")   
print(df.head())
print(df.info())
print(df.describe())

