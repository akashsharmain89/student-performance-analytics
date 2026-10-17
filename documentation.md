# Project Documentation: Student Performance Analytics System

**Student Name:** Akash Sharma  
**Roll Number:**  2503600109003
**Course/Department:** BTech CSE
**Submission Date:** 15/10/26  
**GitHub Repository:** https://github.com/akashsharmain89/student-performance-analytics/tree/main

## 1. Project Title
Student Performance Analytics System

## 2. Objective
The objective is to build a Python program that organizes student marks and attendance data, calculates useful performance statistics, assigns grades, identifies pass/fail status, and highlights top-performing students.

## 3. Technologies Used
- Python 3: program logic, conditions, loops and functions.
- Pandas: loading CSV data, DataFrame operations, grouping and exporting results.
- NumPy: numerical averages and array-based calculations.
- CSV: simple storage format for student records.

## 4. Dataset Description
The project includes 20 sample student records. Columns include Student ID, Name, Department, marks in Python, Mathematics, Data Analysis and AI Basics, and Attendance Percentage. The included data is illustrative sample data.

## 5. Implementation
1. `load_data()` reads `students.csv` with Pandas and checks that required columns exist.
2. `add_student_results()` calculates each student's total and average marks.
3. A grading function assigns A+, A, B, C, D or F based on the student's average.
4. A loop and condition determine pass/fail status. A student passes only when marks in every subject are at least 40.
5. NumPy calculates overall and subject-wise averages.
6. Pandas `nlargest()` identifies the top five students.
7. Pandas `groupby()` calculates average performance by department.
8. The completed analysis is exported to `student_analysis_results.csv`.

## 6. Key Features
- Dataset loading and validation.
- Total and average marks calculation.
- Grade assignment.
- Pass/fail analysis.
- Class, subject and department performance summaries.
- Top-five student ranking.
- Export of processed results to a CSV file.


## 7. Final Outcome
The program turns raw student records into a readable performance summary. It helps identify class-level trends, strong subjects, students needing support and top performers.

## 8. Challenges & Learning
This project practices reading CSV data, working with DataFrames and NumPy arrays, writing reusable functions, using loops and conditions, grouping records, and saving processed results. A possible challenge is keeping column names consistent between the CSV and Python code; the loader checks required columns to help catch this issue.

## 10. GitHub Repository
Repository URL:https://github.com/akashsharmain89/student-performance-analytics/tree/main

## Important
The names and marks provided are demonstration data. Personalize the student details, run and verify the program, capture genuine output screenshots, and ensure the report accurately reflects any changes you make.
