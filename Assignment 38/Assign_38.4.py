# ================================================
# 4. Use value_counts() to analyze the distribution
#    of FinalResult.
#       - Calculate percentage of Pass and Fail students
#       - Check whether the dataset is balanced
#       - Justify your answer
# ================================================

import pandas as pd

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print("Dataset loaded successfully")

# Count how many times each value (0 and 1) appears in FinalResult col
# 1 for pass and 0 for fail

class_counts = df["FinalResult"].value_counts()

print("Class Distribution (Count):")
print(class_counts)
print()


# Calculate percentage distribution of each class
# normalize=True gives ratio (0 to 1), so we multiply by 100 to convert into percentage

class_percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("Class Distribution (Percentage)")
print(class_percentage)
print()

# Get percenatge of pass Students (1)
#if 1 is not present , return 0

pass_percent = class_percentage.get(1,0)


#get  percentage of fail students (0)

fail_percent = class_percentage.get(0,0)

# Check whether dataset is balanced or imbalanced
# If difference between Pass and Fail percentage is less than 10%,
# we consider dataset as balanced

if abs(pass_percent - fail_percent) < 10:
    print("Dataset is BALANCED (Pass and Fail percentages are nearly equal).")
else:
    print("Dataset is IMBALANCED (Significant difference between Pass and Fail).")