# 9. Create a plot showing the relationship between:
#       AssignmentsCompleted and FinalResult
#    Explain your observation..

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print()


result_group = df.groupby("FinalResult")["AssignmentsCompleted"].mean()

plt.figure(figsize=(7,6))
plt.bar(["Fail","Pass"],result_group)
plt.xlabel("FinalResult")
plt.ylabel("Average AssignmentsCompleted")
plt.title("AssignmentsCompleted vs FinalResult")
plt.show()


print("Students who completed more assignments they have more chance  to pass.")
print("The average number of assignments is higher for Pass students.")
print("Students who completed fewer assignments are more likely to fail.")
print("This shows a positive relationship between assignments and success.")