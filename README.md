# Student Performance Analytics System

A beginner-friendly Python mini project that analyzes student marks using **Python, NumPy and Pandas**.

## Features
- Reads student records from `students.csv` into a Pandas DataFrame.
- Calculates total and average marks for each student.
- Assigns grades using a clear grading scale.
- Marks a student Pass only when they score at least 40 in every subject.
- Reports overall class average, highest and lowest averages, pass/fail counts.
- Calculates subject-wise and department-wise averages.
- Displays the top five students.
- Saves all calculated results to `student_analysis_results.csv`.

## Technologies
- Python 3
- NumPy
- Pandas

## Project files
- `main.py` — main program and reusable functions
- `students.csv` — sample dataset of 20 students
- `documentation.md` — project report
- `requirements.txt` — Python dependencies

## Run the project
1. Install Python 3.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```
5. Check the terminal output and the generated `student_analysis_results.csv`.

## Grading rule
- A+: average >= 90
- A: average >= 80 and < 90
- B: average >= 70 and < 80
- C: average >= 60 and < 70
- D: average >= 50 and < 60
- F: average < 50

**Pass condition:** marks must be at least 40 in each of the four subjects. This rule is intentionally explicit and can be adjusted if your instructor gave a different rule.

## Dataset note
The included names and marks are sample data created for demonstration. Replace or edit them if your instructor expects your own dataset. Update this README/report if you change the implementation.

## GitHub submission
Create a public repository named `student-performance-analytics` (or as instructed by your trainer), upload the project files, verify the files are visible, and submit the repository URL through the course Google Form. Do not forget to add your own student details where required.
