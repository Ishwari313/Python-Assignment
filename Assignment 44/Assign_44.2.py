import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def DisplayInfo(title):

    print("\n"+"="*50)
    print(title)
    print("="*50)


def ShowData(df,message):

    DisplayInfo(message)

    print("First five rows from dataset:")
    print(df.head())

    print("Shape of Dataset:")
    print(df.shape)

    
    print("\nMissing value from dataset")
    print(df.isnull().sum())

    print("Columns Names:")
    print(df.columns.tolist())

def CleanData(df):

    DisplayInfo("Step 2 : Original Data")
    print(df.head())
    print(df.shape)

    print("Data after removal")

    if "Unnamed: 0" in df.columns:
        df.drop(columns =["Unnamed: 0"],inplace = True)

    print("Data after removal that unmaned column")
    print(df.shape)

def Casestudy(Datapath):
    DisplayInfo("Step 1: Load the Dataset")
    df = pd.read_csv(Datapath)
    ShowData(df,"Initial Dataset")

    df = CleanData(df)


def main():

    Casestudy("Advertising.csv")

if __name__ =="__main__":
    main()