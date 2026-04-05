# ===========================================================
# 5. Based on the dataset values, analyze whether:
#       - Higher StudyHours increase the chance of passing
#       - Higher Attendance improves FinalResult
#    Write observations in 4–5 lines
# ============================================================

# Students with higher StudyHours generally have a higher probability of passing the exam.

# As StudyHours increase, the number of students with FinalResult = 1 also increases.

# Higher Attendance is positively associated with better FinalResult outcomes.

# Students with low attendance are more likely to fail compared to those with regular attendance.

# Therefore, both StudyHours and Attendance show a positive impact on passing chances.

import pandas as pd

print("Step 1 : Load the dataset")

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print()

print("Total number of rows is :",df.shape[0])
print("Total number of columns is :",df.shape[1])

print()

print("Column from dataset is :",df.columns)