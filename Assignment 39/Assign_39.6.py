# 6. Train Decision Tree models with different max_depth values.
# This helps analyze the effect of model complexity on performance.



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*50

# Step 1 :Load the Dataset

print(Border)
print("Step 1: Load the Dataset")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print("Dataset gets loaded successfully..")




print(Border)
print("Decides independant and dependant variables")
print(Border)

# X: independent variables
# Y : Dependent

feature_cols = [

    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

print("X shape :",X.shape)
print("Y shape :",Y.shape)

print()

print(Border)
print("Split the dataset for training and testing")
print(Border)

X_train , X_test, Y_train,Y_test= train_test_split(
    X,Y, test_size=0.2,random_state=42
)

print("X - Independant : ",X.shape) # (150,4)
print("Y - Dependant : ",Y.shape)   # (150,)

print()

print("X_train : ",X_train.shape)   # (120,4)
print("X_test : ",X_test.shape)     # (30,4)

print()

print("Y_train : ",Y_train.shape)   # (120,)
print("Y_test : ",Y_test.shape)     # (30,)

print()


print(Border)
print("Step 6 : Build the Model")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth = 2,
    random_state = 42

)

print("Model succesfully created : ",model)



print(Border)
print("Step 7 : Train the Model")
print(Border)


print()

model.fit(X_train,Y_train)

print("Model training completed...")

print()


print(Border)
print("Step 8 : Test the Model")
print(Border)

print()

Y_pred = model.predict(X_test)

print("Model testing completed")

print(Y_pred.shape)
print("Expected ans :")
print(Y_test)

print("Predicted ans:")
print(Y_pred)


print(Border)
print("Step 9 : Evaluate the model Performance")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy score is :",accuracy*100 ,"%")

CM = confusion_matrix(Y_test,Y_pred)

print("Confusion Matrix : ")  
print(CM)


# Training accuracy
Y_train_pred = model.predict(X_train)

train_accuracy = accuracy_score(Y_train,Y_train_pred)

# Testing accuracy
Y_test_pred = model.predict(X_test)

test_accuracy = accuracy_score(Y_test,Y_test_pred)

print("Training accuracy : ",train_accuracy*100,"%")
print("Testing accuracy : ",test_accuracy*100,"%")