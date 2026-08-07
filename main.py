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

# intilize required variables:
total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

for day in range(1, 8):
    while True:
        score = int(input(f"Enter Day {day} score from 0 to 100 or -1 for absent: "))
        if score == -1 or 0<=score<=100:
            print("Score accepted")
            break
        else:
            print("Invalid score. Enter -1 or a value between 0 and 100.")
    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
        continue

    attempted_days += 1
    total_score += score
    if score>=60:
        passed_days+=1
    else:
        failed_days+=1

    if score >= 75:
        strong_days += 1
        print(f"Day {day} Result: Strong")
    elif score >= 60:
        satisfactory_days += 1
        print(f"Day {day} Result: Satisfactory")
    elif score >= 40:
        improvement_days += 1
        print(f"Day {day} Result: Needs Improvement")
    else:
        critical_days += 1
        print(f"Day {day} Result: Critical")
        if not critical_score_found:
            critical_score_found=True
            first_critical_day =day
            first_critical_score=score

    if not first_attempt_found:
        highest_score=lowest_score=score
        highest_score_day=lowest_score_day=day
        first_attempt_found=True
    else:
        if score>highest_score:
            highest_score=score
            highest_score_day=day
        if score<lowest_score:
            lowest_score=score
            lowest_score_day=day  
    
