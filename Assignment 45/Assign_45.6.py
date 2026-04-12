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

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("Information about Training data and testing data:")

    print()

    print("X_train shape :",X_train)
    print("X_test shape:",X_test)
    print("Y_train shape:",Y_train)
    print("Y_test shape:",Y_test)

    
# step 5 : Feature Engineering

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature scalinf Done")

# step 6 : Explore the values of K

    print(Border)
    print("Step 6 : Explore the Multiple value of K")
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train_scaled,Y_train)

        y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(y_pred, Y_test)
        accuracy_scores.append(accuracy)

    print("Accuracy of all k from 1 to 20")

    for value in accuracy_scores:
        print(value)

# step 7 : Plot the graph

    print(Border)
    print("Step 7 : plot the graph")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = 'o')
    plt.title("K Value vs Accuracy")
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))

    plt.show()

# step 8: find best k

    print(Border)
    print("Step 8 : Find of best k")
    print(Border)

    best_k = list(K_values)[accuracy_score.index(max(accuracy_scores))]

    print("Best value of k is :",best_k)


# step 9 : Build the Final model

    print(Border)
    print("Step 9 : Build the final model using best of k")
    print(Border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)

    model.fit(X_train_scaled,Y_train)
    y_pred = model.predict(X_test_scaled)

# step 10 : Calculate the final accuracy

    print(Border)
    print("Step 10 : Calculate final accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test,y_pred)
    print("The Accuracy of the model is :",accuracy*100)

# Step 11: Display the confudion matrix

    print(Border)
    print("Step 11 : Display the confusion matrix")
    print(Border)

    cm = confusion_matrix(Y_test,y_pred)
    print(cm)

# Step 12 : Display the classification report

    print(Border)
    print("Step 12 :Display the Classification report")
    print(Border)

    print(classification_report(Y_test,y_pred))
    
     
def main():

    Wineclassifier("WinePredictor.csv")
if __name__ =="__main__":
    main()