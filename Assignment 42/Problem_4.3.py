import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def main():

    X_train =[[1],[2],[3],[4],[5]] # Independent variable

    Y_train=[2000,25000,30000,35000,40000]

    # Test the data

    X_test =[[6]]
    Y_test=[50000]

    model = LinearRegression()

    model.fit(X_train,Y_train)

    y_pred=model.predict(X_test)

    print("Predicted salary for 6 yrs:",y_pred[0])

    # mean squared error

    MSE= mean_squared_error(Y_test,y_pred)
    print("Mean squared error is:",MSE)

    # graph
    plt.figure(figsize=(7,6))

    plt.scatter(X_train,Y_train)
    plt.scatter(X_test,y_pred)

    Y_line = model.predict(X_train)
    plt.plot(X_train,Y_line)

    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")

    plt.legend()
    
    plt.grid(True)

    plt.show()


if __name__=="__main__":
    main()