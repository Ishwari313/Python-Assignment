import pandas as pd
import matplotlib as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


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

def main():

    Wineclassifier("WinePredictor.csv")
if __name__ =="__main__":
    main()