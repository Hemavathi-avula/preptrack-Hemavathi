# PrepTrack — Placement Preparation Performance Analyzer

## 1. Project Overview

PrepTrack is a Python console-based application designed to evaluate a student's placement preparation performance. It collects student profile details, attendance, graduation year, project completion status, profile verification status, and seven days of coding practice scores. The application validates the entered information, analyzes practice performance, calculates scores and averages, and determines the student's placement readiness. It also identifies the primary blocker and recommends the next action when the student is not ready.

---

## 2. Features Implemented

The application includes the following features:

* Student profile input
* Student name validation
* Registration number input
* Graduation year validation
* Attendance validation between 0 and 100
* Project completion Yes/No validation
* Profile verification Yes/No validation
* Seven-day coding practice processing
* Practice score validation
* Absent-day handling
* Passed and failed practice counting
* Score classification
* Strong score detection
* Satisfactory score detection
* Needs Improvement detection
* Critical score detection
* Highest score detection
* Lowest score detection
* First critical score detection
* Total score calculation
* Average score calculation
* Practice eligibility evaluation
* Attendance eligibility evaluation
* Graduation eligibility evaluation
* Project completion eligibility
* Profile verification eligibility
* Placement-readiness evaluation
* Final status generation
* Primary blocker identification
* Next action recommendation
* Final performance report generation

---

## 3. Score Classification

The application classifies each attempted practice score as follows:

| Score Range | Classification    |
| ----------- | ----------------- |
| 75–100      | Strong            |
| 60–74       | Satisfactory      |
| 40–59       | Needs Improvement |
| 0–39        | Critical          |
| -1          | Absent            |

A score of `-1` represents an absent practice day and is not included when calculating the average score.

---

## 4. Placement Readiness Criteria

The application evaluates placement readiness using multiple conditions.

A student must satisfy the following requirements:

* Graduation year must be between 2025 and 2027.
* Attendance must be at least 75%.
* At least 6 practice days must be attempted.
* Average practice score must be at least 70.
* At least 4 practice days must be passed.
* No critical score should be present.
* Required project must be completed.
* Student profile must be verified.

If a requirement is not satisfied, PrepTrack identifies the primary blocker and provides a recommended next action.

---

## 5. Python Concepts Used

The project uses the following Python concepts:

* Variables
* Strings
* Integers
* Floating-point numbers
* Boolean values
* `input()`
* `print()`
* Type conversion using `int()` and `float()`
* Arithmetic operators
* Relational operators
* Logical operators
* Assignment operators
* Boolean expressions
* `if`, `elif`, and `else`
* Nested conditions
* `while` loops
* `for` loops
* `range()`
* `break`
* `continue`
* Counters
* Accumulator variables
* Conditional expressions
* f-Strings
* Input validation

---

## 6. How to Run

### Step 1: Open the project folder

Open the PrepTrack project folder in a terminal or command prompt.

### Step 2: Run the program

```bash
python main.py
```

If your system uses Python 3:

```bash
python3 main.py
```

### Step 3: Enter the required information

The application will ask for:

* Student name
* Registration number
* Graduation year
* Attendance percentage
* Project completion status
* Profile verification status
* Seven daily practice scores

Use `-1` when the student is absent on a practice day.

### Step 4: View the final report

After all inputs are entered, the application displays the student's profile, practice summary, performance analysis, critical-score information, final status, primary blocker, and next recommended action.

---

## 7. Test Result Summary

The application was tested using valid and invalid inputs to verify the validation, calculation, and decision-making logic.

| Test Scenario                   | Status |
| ------------------------------- | ------ |
| Student Name Validation         | Passed |
| Registration Number Input       | Passed |
| Graduation Year Validation      | Passed |
| Attendance Validation           | Passed |
| Project Status Validation       | Passed |
| Profile Verification Validation | Passed |
| Practice Score Validation       | Passed |
| Absent Day Handling             | Passed |
| Score Classification            | Passed |
| Passed and Failed Count         | Passed |
| Highest Score Detection         | Passed |
| Lowest Score Detection          | Passed |
| Critical Score Detection        | Passed |
| Average Calculation             | Passed |
| Placement Readiness Evaluation  | Passed |
| Final Report Generation         | Passed |

---

## 8. Individual Contribution

**Name:** Avula Hemavathi

**Repository URL:**
https://github.com/Hemavathi-avula/preptrack-Hemavathi.git

### My Main Contribution

I worked on the development of the PrepTrack Python console application, including student-profile input, input validation, seven-day practice score processing, performance analysis, placement-readiness evaluation, and final report generation.

### Features I Implemented

* Student name validation
* Registration number input
* Graduation year validation
* Attendance validation
* Project completion validation
* Profile verification validation
* Seven-day practice score processing
* Absent-day handling
* Passed and failed practice counting
* Score classification
* Highest and lowest score detection
* Critical-score detection
* Average score calculation
* Placement-readiness evaluation
* Primary blocker identification
* Next action recommendation
* Final report generation

### Python Concepts I Used

* Variables and data types
* User input
* Type conversion
* Conditional statements
* `for` loops
* `while` loops
* `break`
* `continue`
* Boolean expressions
* Relational operators
* Logical operators
* Counters
* Accumulator variables
* f-Strings
* Input validation

### Most Difficult Logic

The most difficult part was processing the seven daily practice scores while tracking multiple values such as attempted days, absent days, passed days, failed days, highest score, lowest score, and critical scores.

The placement-readiness decision was also challenging because several conditions had to be checked together and the application needed to identify the correct primary blocker.

### Problem I Faced

I initially faced problems with Python indentation, variable-name inconsistencies, Boolean values, and combining multiple eligibility conditions.

I also needed to make sure absent days were not included in the average calculation and that highest and lowest scores were calculated only from attempted days.

### How I Solved It

I divided the program into smaller sections and tested each part separately. I used counters and Boolean variables to track different conditions and used `break` and `continue` to control the loops. I also used logical operators to combine the placement-readiness requirements.

---

## 9. Code Review Completed

A peer code review was completed to identify logical errors, input-validation issues, variable inconsistencies, and opportunities to improve the readability and reliability of the application.

### Review Areas

* Input validation
* Variable naming
* Score processing
* Score classification
* Average calculation
* Highest and lowest score calculation
* Placement-readiness conditions
* Final status logic
* Code readability

---

## 10. Feedback Received

The following feedback was received during the code review:

1. Improve input validation so invalid values are handled properly.
2. Maintain consistent variable names throughout the program.
3. Ensure Boolean values are used consistently.
4. Display the daily practice result after processing each score.
5. Make final status messages clearly represent the student's actual placement-preparation condition.
6. Improve the readability of the final decision logic.

### Was the Feedback Valid?

Yes. The feedback helped identify areas where the program could be made more consistent, readable, and user-friendly.

---

## 11. Improvement Made After Review

Based on the peer-review feedback, improvements were made to the validation and decision-making logic.

### Improvements

* Corrected variable-name inconsistencies.
* Improved indentation and code structure.
* Used Boolean values consistently for project and profile status.
* Added daily practice result messages.
* Improved handling of absent practice days.
* Improved highest and lowest score tracking.
* Updated final status and next-action messages.
* Improved the placement-readiness decision logic.

### Example of Improved Placement Decision

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

### Commit Message Used

```bash
git commit -m "Apply peer review improvements"
```

---

## 12. Project Structure

```text
PrepTrack/
│
├── main.py
└── README.md
```

---

## 13. Conclusion

PrepTrack demonstrates how fundamental Python concepts can be used to build a practical placement-preparation analysis application. The project validates student information, analyzes seven days of coding practice, evaluates multiple eligibility conditions, and provides a clear placement-readiness result with a recommended next action.
