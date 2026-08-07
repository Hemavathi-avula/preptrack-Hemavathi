# my first Project
print("=" * 50)
print("        PREPTRACK APPLICATION")
print("=" * 50)
print()
while True:
    student_name = input("Enter student name: ")
    if student_name != "":
        break
    print("Student name should not be empty ")
# Registration number details
registration_number = input("Enter registration number: ")
# graduation deatails
while True:
    graduation_year = int(input("Enter graduation year: "))
    if graduation_year >= 2025 and graduation_year <=2027:
        break
    print("enter correct graduation year")
graduation_eligible=(graduation_year>=2025 and graduation_year<=2027)
# attandance details
while True:
    attendance = float(input("Enter attendance percentage: "))
    if attendance >= 0 and attendance <= 100:
        break
    print("Invalid attandance")
# project details
while True:
    project_status = input(
        "Has the student completed the required project?"
        "Enter yes or no: ").lower()
    if project_status == "yes":
        project_status = True
        break
    elif project_input == "no":
        project_input = False
        break
    print("Enter valid input")
# profile verification:
while True:
    profile_verification = input("Is the student profile verified?"
                               "Enter yes or no: ").lower()
    if profile_verification == "yes":
        profile_verification = True
        break
    elif profile_verification == "no":
        profile_verification = False
        break
    print("Enter valid input")
    
