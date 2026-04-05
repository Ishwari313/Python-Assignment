# ================================================
# 6. Plot a histogram of StudyHours.
#    Explain what the distribution tells you.
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print()

sns.histplot(data= df,x="StudyHours")

plt.xlabel("StudyHours")
plt.ylabel("Number of Students")
plt.title("Distribution of study Hours")

plt.show()