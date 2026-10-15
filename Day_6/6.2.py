student = {}

student["name"] = input("Enter student name: ")
student["assignment"] = float(input("Enter assignment marks: "))
student["lab"] = float(input("Enter lab marks: "))
student["test"] = float(input("Enter test marks: "))

total = student["assignment"] + student["lab"] + student["test"]
percentage = total / 3

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("\nStudent Details")
print("Name:", student["name"])
print("Assignment Marks:", student["assignment"])
print("Lab Marks:", student["lab"])
print("Test Marks:", student["test"])
print("Percentage:", percentage)
print("Grade:", grade)