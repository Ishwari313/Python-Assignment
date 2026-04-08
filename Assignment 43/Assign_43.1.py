import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score,confusion_matrix,classification_report
)

Border = "-"*50

# Step 1 . Load the Dataset
print(Border)
print("Step 1 :Load the Dataset")
print(Border)

Dataset ="PlayPredictor.csv"

df = pd.read_csv(Dataset)

print("Dataset loaded")

print(df.head())
