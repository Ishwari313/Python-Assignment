# 8. Draw a boxplot for Attendance.
#    Identify whether any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print()

# Box plot

plt.figure(figsize=(7,6))
plt.boxplot(df["Attendance"])
plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")
plt.show()

#Observation

print("In the boxplot, any points shown outside the whiskers are outliers.")
print("If there are dots above or below the whiskers, then outliers are present.")
print("If no points appear outside the whiskers, then no outliers exist.")