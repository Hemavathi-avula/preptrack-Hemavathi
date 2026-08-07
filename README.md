
# PrepTrack — Placement Preparation Performance Analyzer

# 1. Project Overview

PrepTrack is a Python-based application that analyzes a student's placement preparation performance. 
It collects student profile details such as registration number, graduation year, attendance, project completion, and profile verification. The application also processes seven days of coding practice scores, classifies performance, calculates overall performance, and checks placement eligibility. 
Finally, it displays a detailed report containing the student's performance, blockers, and recommended next action.


## 2. Features Implemented

The application includes the following features:

* Student-profile input
* Student name validation
* Registration number input
* Graduation-year validation
* Attendance validation between 0 and 100
* Yes-or-no input validation
* Project completion verification
* Profile verification
* Seven-day practice score processing
* Absent-day tracking
* Passed and failed practice counting
* Score classification
* Strong-score detection
* Satisfactory-score detection
* Needs-improvement detection
* Critical-score detection
* Highest score detection
* Lowest score detection
* First critical score detection
* Average score calculation
* Practice eligibility evaluation
* Attendance eligibility evaluation
* Graduation eligibility evaluation
* Project completion eligibility
* Profile verification eligibility
* Placement-readiness evaluation
* Final status generation
* Primary blocker identification
* Next-action recommendation
* Detailed final performance report

---

## 3. Score Classification

The application classifies daily practice scores using the following criteria:

| Score Range | Classification    |
| ----------- | ----------------- |
| 75–100      | Strong            |
| 60–74       | Satisfactory      |
| 40–59       | Needs Improvement |
| 0–39        | Critical          |

A score of `-1` represents an absent practice day.

---

## 4. Placement Readiness Criteria

The application checks multiple conditions before considering a student ready for placement preparation.

The main eligibility conditions are:

* Graduation year must be between 2025 and 2027.
* Attendance must be at least 75%.
* At least 6 practice days must be attempted.
* Average practice score must be at least 70.
* At least 4 practices must be passed.
* No critical score should be present.
* Required project must be completed.
* Student profile must be verified.

If the conditions are not satisfied, the application identifies the primary blocker and provides a recommended next action.

---

## 5. Python Concepts Used

The following Python concepts were used in the project:

* Variables
* Data types
* `input()` function
* `print()` function
* Type conversion using `int()` and `float()`
* Arithmetic operators
* Comparison operators
* Logical operators
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* `break`
* `continue`
* Boolean values
* String methods such as `.lower()`
* Formatted strings using f-strings
* Conditional expressions
* Counters
* Basic input validation

---

## 6. How to Run

### Step 1: Clone the repository

Clone the project repository to your computer.

### Step 2: Open the project folder

Open the project folder in a terminal or command prompt.

### Step 3: Run the program

```bash
python main.py
```

Depending on the system configuration:

```bash
python3 main.py
```

### Step 4: Enter the requested information

The application will ask for student details, attendance, project status, profile verification, and seven daily practice scores.

### Step 5: View the final report

After entering all required information, PrepTrack displays the student's performance summary and placement-readiness decision.

---

## 7. Test-Result Summary

The application was tested with different types of input to verify the validation and decision-making logic.

### Test Case 1 — Valid Student Profile

**Input:**

* Valid student name
* Valid graduation year
* Valid attendance
* Project completed
* Profile verified

**Result:**
The application accepts the student details successfully.

### Test Case 2 — Invalid Attendance

**Input:**

```text
Attendance = 105
```

**Result:**
The application rejects the value and asks the user to enter attendance between 0 and 100.

### Test Case 3 — Invalid Practice Score

**Input:**

```text
Score = 120
```

**Result:**
The application rejects the score and asks for a value between 0 and 100 or `-1` for absence.

### Test Case 4 — Absent Practice Day

**Input:**

```text
Score = -1
```

**Result:**
The day is recorded as absent and is not included in the average score calculation.

### Test Case 5 — Critical Score

**Input:**

```text
Score = 30
```

**Result:**
The score is classified as Critical, and the application records the first critical score.

### Test Case 6 — Placement Readiness

When the student satisfies all required eligibility conditions, the application displays:

```text
Final Status    : Ready for Mock Interview
Primary Blocker : None
```

---

## 8. Individual Contribution

# Name: Avula Hemavathi

**Repository URL:**


**My main contribution:**
I worked on the student input, validation, seven-day practice processing, score analysis, and placement-readiness logic of the PrepTrack application.

**Features I implemented:**

* Student name validation
* Registration number input
* Graduation-year validation
* Attendance validation
* Project completion validation
* Profile verification
* Seven-day practice score processing
* Absent-day tracking
* Passed and failed practice counting
* Score classification
* Highest and lowest score detection
* Critical-score detection
* Average score calculation
* Placement-readiness evaluation
* Final status and next-action generation

**Python concepts I used:**

I used variables, input/output, type conversion, conditional statements, `for` and `while` loops, Boolean values, comparison operators, logical operators, `break`, `continue`, f-strings, and input validation.

**Most difficult logic:**

The most difficult part was implementing the seven-day practice score analysis and placement-readiness decision. The application needs to track several values at the same time, such as attempted days, absent days, passed days, failed days, average score, highest score, lowest score, and critical scores.

**Problem I faced:**

I initially had problems with indentation, variable names, and handling the project-status value consistently. I also needed to understand how multiple eligibility conditions should be combined to make the final placement decision.

**How I solved it:**

I divided the application into smaller sections and tested each section separately. I used counters and Boolean variables to track the student's performance and used logical operators to combine the eligibility conditions. I also corrected variable-name inconsistencies and improved input validation.

---

## 9. Code Review Completed

The project code was reviewed to identify logical errors, validation issues, variable inconsistencies, and opportunities for improvement.

The review focused on:

* Input validation
* Variable naming
* Conditional logic
* Score calculation
* Placement-readiness conditions
* Code readability
* Handling invalid input

---

## 10. Feedback Received

The following improvements were identified during the code review:

* Maintain consistent variable names throughout the program.
* Use proper indentation for Python blocks.
* Validate user input before processing it.
* Keep Boolean values consistent instead of comparing them with strings.
* Improve handling of invalid numeric input.
* Make the final decision logic easier to understand.

---

## 11. Improvement Made After Review

After the review, the input-validation and decision logic were improved.

For example, the project-status value is stored consistently as a Boolean:

```python
if project_status == "yes":
    project_status = True
elif project_status == "no":
    project_status = False
```

The placement-readiness condition then uses the Boolean value directly:

```python
placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_status
    and profile_verification
)
```

This makes the code more consistent, readable, and easier to maintain.

---

## 12. Project Structure

```text
PrepTrack/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 13. Conclusion

PrepTrack provides a simple way to evaluate a student's placement preparation progress. It combines profile validation, attendance, coding-practice performance, project completion, and profile verification to produce a final readiness decision. The project demonstrates the practical use of fundamental Python programming concepts in a real-world application.

