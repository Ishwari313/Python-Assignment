# WRITE A PROGRAM WHICH ACCEPTS MARKS AND DISPLAY GRADE
Marks=int(input("Enter The Marks:"))

if Marks < 0 or Marks>100:
    print("Invalid marks")
    
elif Marks >=75:
    print("Distinction")

elif Marks>=60:
    print("First Class")

elif Marks >=50:
    print("Second class")

else:
    print("Fail")