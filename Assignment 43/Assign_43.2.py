import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
)

from sklearn.preprocessing import LabelEncoder

Border = "-"*50

# Step 1 . Load the Dataset

print(Border)
print("Step 1 :Load the Dataset")
print(Border)

Dataset ="PlayPredictor.csv"

df = pd.read_csv(Dataset)

print("Dataset loaded")

print(df.head())


# Step 2: Clean the Data(EDA)

print(Border)
print("Step 2 : Data Cleaning (EDA)")

# remove column

print("Shape of data before cleaning :",df.shape)

if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"],inplace=True)

print("Shape of Data after cleaning:",df.shape)

print("Clean Dataset is:",df.head())

#missing values

print("Check missing values:",df.isnull().sum())


# manipulate the data

print("Data before manipulation:",df.head())

LE= LabelEncoder()
df['Whether'] = LE.fit_transform(df['Whether'])
df['Temperature']= LE.fit_transform(df['Temperature'])
df['Play'] = LE.fit_transform(df['Play'])

print("Data after Manipulation:",df.head())

