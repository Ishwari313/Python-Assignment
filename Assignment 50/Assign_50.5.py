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



from sklearn.preprocessing import LabelEncoder, StandardScaler

# Replace 'unknown' with NaN and fill with mode
df = df.replace("unknown", np.nan)
df = df.fillna(df.mode().iloc[0])

# Separate features & target
X = df.drop("y", axis=1)
y = df["y"]

# Encode categorical columns
cat_cols = X.select_dtypes(include=['object']).columns
num_cols = X.select_dtypes(include=['int64','float64']).columns

# Label Encoding for simplicity
le = LabelEncoder()
for col in cat_cols:
    X[col] = le.fit_transform(X[col])

# Scale numeric features
scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])


from sklearn.preprocessing import LabelEncoder, StandardScaler

# Replace 'unknown' with NaN and fill with mode
df = df.replace("unknown", np.nan)
df = df.fillna(df.mode().iloc[0])

# Separate features & target
X = df.drop("y", axis=1)
y = df["y"]

# Encode categorical columns
cat_cols = X.select_dtypes(include=['object']).columns
num_cols = X.select_dtypes(include=['int64','float64']).columns

# Label Encoding for simplicity
le = LabelEncoder()
for col in cat_cols:
    X[col] = le.fit_transform(X[col])

# Scale numeric features
scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "KNN": KNeighborsClassifier(),
    "Random Forest": RandomForestClassifier()
}

trained_models = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    trained_models[name] = model
    print(f"{name} trained successfully.\n")

    