import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np

def TrainData(df):

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("\nIndependent Variables")
    print(X.head())

    print("\nDependent Variables")
    print(Y.head())

    print("Shape of X :",X.shape)
    print("Shape of Y:",Y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(X, Y,random_state=42,test_size=0.2)

    print("X_train Shape :",X_train.shape)
    print("X_test Shape :",X_test.shape)
    print("Y_train Shape :",Y_train.shape)
    print("Y_test Shape :",Y_test.shape)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print("Model Trained")



    MSE = mean_squared_error(Y_test,Y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test,Y_pred)

    print("Mean Squared error :",MSE)
    print("Root Mean Squared error :",RMSE)
    print("R sqaure value :",R2)



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

    return df

def Casestudy(Datapath):
    DisplayInfo("Step 1: Load the Dataset")
    df = pd.read_csv(Datapath)
    ShowData(df,"Initial Dataset")

    df = CleanData(df)

    TrainData(df)


def main():

    Casestudy("Advertising.csv")

if __name__ =="__main__":
    main()