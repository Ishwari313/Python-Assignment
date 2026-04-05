# 10. Plot SleepHours against FinalResult.
#     Does sleeping more guarantee success?
#     Explain your answer.


# 9. Create a plot showing the relationship between:
#       AssignmentsCompleted and FinalResult
#    Explain your observation..

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print()

sns.scatterplot(
    data=df,
    x="SleepHours",
    y="FinalResult",
    
)

plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.title("SleepHours VS FinalResult ")

plt.legend(title="Final Result (0=Fail, 1=Pass)")
plt.show()


print("Sleeping more does not guarantee success.")
print("Both pass and fail students have similar sleep ranges.")
print("There is no strong visible pattern between SleepHours and FinalResult.")
print("Sleep is important, but other factors like StudyHours and Attendance")
print("have a stronger impact on success.")