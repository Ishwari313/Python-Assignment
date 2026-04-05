# ================================================
# 3. Using pandas functions, calculate and display:
#       - Average StudyHours
#       - Average Attendance
#       - Maximum PreviousScore
#       - Minimum SleepHours
# ================================================

import pandas as pd

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

avg_StudyHrs = df["StudyHours"].mean()
avg_attendence = df["Attendance"].mean()
max_prev_score = df['PreviousScore'].max()
min_sleepHrs = df["SleepHours"].min()


print("Average Study Hours :",avg_StudyHrs)
print("Average Attendence :",avg_attendence)
print("Maximum Previous Scors :",max_prev_score)
print("Minimum Sleep Hours:",min_sleepHrs)