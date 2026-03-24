tc = int(input("Enter the total number of classes that have happened: "))
ca = int(input("Enter the number of classes attended: "))
rc = int(input("Enter the number of classes left: "))
study_hrs = float(input("Enter hours studied daily: "))
sleep_hrs = float(input("Enter hourse slept daily: "))

ap = (ca/tc)*100

final = tc + rc
required = final*0.75
max_att = ca + rc

max_leaves = max_att - required

if ca > tc:
    print("Error:Attened classes can't be more then total classes")



if max_leaves >=0:
    status = "Will not be debarred"
else:
    status = "You need to attend all classes to imporove your attendance and maybe not be debarred"

print("--- RESULT ---")
print(f"Current Attendance: {ap:.2f}%")
print(f"Max Classes You Can Miss: {max_leaves:.2f}")
print(f"Status: {status}")