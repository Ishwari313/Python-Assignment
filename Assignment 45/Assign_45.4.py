import pandas as pd
import matplotlib as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def Wineclassifier(datapath):
    Border = "="*50
    df = pd.read_csv(datapath)


# Step 1 : Load the Dataset

    print(Border)

    print("Step 1 : Load the Dataset")
    print(Border)

    print("5 entries from the dataset")
    print(df.head())

    print("COlumns of Dataset")
    print(df.columns.tolist())

    print("Shape of dataset:")
    print(df.shape)

# step 2: CLean the Data

    print(Border)
    print("Step 2 : Clean the data")
    print(Border)

    print()

    print("Shape of data before remoavl")
    print(df.shape)
    print()

    df.dropna(inplace = True)
    print("Total Records :",df.shape[0])
    print("Total Columns:",df.shape[1])

    print()

    print("Shape of dataset after removel:")
    print(df.shape)


# Step 3 : Decide the independent and dependent variable

    print(Border)
    print("Step 3 : Decides independent and dependent variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Independent Variables :")
    print(X.head())

    print()

    print("Dependent Variavbles:")
    print(Y.head())

    print()

    print("Shape of X :",X.shape)
    print("Shape of Y:",Y.shape)

    print()

    print("Input Columns:",X.columns.to_list())
    print("Output Columns : Class")


# Step 4 : Split the dataset for training and testing

    print(Border)
    print("Step 4 : Split the dataset for training and testing the data")
    print(Border)

    X_train,Y_train, X_test, Y_test = train_test_split(X, Y, test_size=0.2,random_state=42)

    print("Information about Training data and testing data:")

    print()

    print("X_train shape :",X_train)
    print("X_test shape:",X_test)
    print("Y_train shape:",Y_train)
    print("Y_test shape:",Y_test)

    
def main():

    Wineclassifier("WinePredictor.csv")
if __name__ =="__main__":
    main()