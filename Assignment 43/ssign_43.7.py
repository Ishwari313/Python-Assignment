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

# Step 3 :independent nd dependent vrible


print(Border)
print("Step 3 : Decides independant and dependant variables")
print(Border)

# X : Independant varibales(features)
# Y : Dependant variballs (labels)

feature_cols = [

    "Whether",
    "Temperature"
]

X = df[feature_cols]
Y = df["Play"]

print("X shape :",X.shape)
print("Y shape :",Y.shape)

#step 4: split the dtset for trining nd testing

print(Border)
print("Step 4 : Split the dataset for training and testing")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

print("X_train :",X_train.shape)
print("X_test :",X_test.shape)

print("Y_train :",Y_train.shape)
print("Y_test :",Y_test.shape)

#step 5: build model

print(Border)
print("Step 5 : Build the Model")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

print("Model succesfully Created :",model)

# trin model

print(Border)
print("Step 5 : Trin the Model")
print(Border)

model.fit(X_train,Y_train)

# test model
print(Border)
print("Step 8 : Test the Model")
print(Border)

y_pred = model.predict(X_test)

print("Model testing complete :")

print(y_pred.shape)

print("Expected answer :")
print(Y_test)

print("Predicted answer : ")
print(y_pred)

#check the performnce


print(Border)
print("Step 8 : Evaluate the model performance")
print(Border)

accuracy = accuracy_score(y_pred,Y_test)

print("Model Accuracy is :",(accuracy*100),"%")