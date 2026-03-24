import pandas as pd

data = pd.read_csv("Fundamentals_AI_ML_Project/Attendance_data.csv")

data["Total_Classes"]= data["total_classes_happened"]+ data["remaining_classes"]

data["Required_Attendance"]= data["Total_Classes"]*0.75

data["Max_Possible_Attendance"]= data["classes_attended"]+ data["remaining_classes"]

data["Max_leaves"]=(data["Max_Possible_Attendance"] - data["Required_Attendance"]).round(1)

data["Attendance_Percentage"]=((data["classes_attended"]/data["total_classes_happened"])*100).round(1)

def Status(x):
    if x>=0:
        return "Will not be debarred"
    else:
        return "Will be debarred"
    
data["Status"] = data["Max_leaves"].apply(Status)

print(data.head())

print("Mean attendance:", data["Attendance_Percentage"].mean())
print("Variance:", data["Attendance_Percentage"].var())
print("Standard Deviation:", data["Attendance_Percentage"].std())
