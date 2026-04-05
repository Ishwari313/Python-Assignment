# ================================================
# 7. Create a scatter plot of:
#    StudyHours vs PreviousScore
#    Use different colors for Pass and Fail students.
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print()

sns.scatterplot(
    data=df,
    x= "StudyHours",
    y = "PreviousScore",
    hue="FinalResult",
    palette={0: "red",1:"green"}
)

plt.xlabel("Study Hours")
plt.ylabel("PreviousScore")
plt.title("Study Hours VS PreviousScore")


plt.legend(title="Final Result (0=fail, 1=pass)")
plt.show()