"""
Student Performance Analytics System
Python + NumPy + Pandas mini project.

Run:
    pip install -r requirements.txt
    python main.py
"""
import numpy as np
import pandas as pd

DATA_FILE = "students.csv"
SUBJECTS = ["Python", "Mathematics", "Data_Analysis", "AI_Basics"]
PASS_MARK = 40  # A student passes only if they score at least 40 in every subject.


def load_data(file_path=DATA_FILE):
    """Load the CSV dataset and validate the expected columns."""
    df = pd.read_csv(file_path)
    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance_Percent"]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")
    return df


def add_student_results(df):
    """Return a copy of the dataset with totals, averages, grades and status."""
    result = df.copy()
    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = np.round(result[SUBJECTS].mean(axis=1), 2)

    def assign_grade(average):
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        return "F"

    result["Grade"] = [assign_grade(avg) for avg in result["Average_Marks"]]
    # Passing requires PASS_MARK or above in every subject.
    result["Result"] = [
        "Pass" if all(mark >= PASS_MARK for mark in marks) else "Fail"
        for marks in result[SUBJECTS].to_numpy()
    ]
    return result


def show_overall_summary(results):
    """Print overall class statistics."""
    averages = results["Average_Marks"].to_numpy()
    passed = int((results["Result"] == "Pass").sum())
    failed = int((results["Result"] == "Fail").sum())
    print("\n" + "=" * 66)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 66)
    print(f"Total students       : {len(results)}")
    print(f"Students passed      : {passed}")
    print(f"Students failed      : {failed}")
    print(f"Class average        : {np.mean(averages):.2f}")
    print(f"Highest student avg  : {averages.max():.2f}")
    print(f"Lowest student avg   : {averages.min():.2f}")


def show_subject_analysis(results):
    """Display mean marks for each subject."""
    print("\nSUBJECT-WISE AVERAGE")
    for subject in SUBJECTS:
        subject_average = np.mean(results[subject].to_numpy())
        print(f"{subject.replace('_', ' '):20s}: {subject_average:.2f}")


def show_top_performers(results, count=5):
    """Display students ranked by average marks."""
    print(f"\nTOP {count} PERFORMING STUDENTS")
    top = results.nlargest(count, "Average_Marks")
    print(top[["Student_ID", "Name", "Department", "Average_Marks", "Grade"]].to_string(index=False))


def show_department_analysis(results):
    """Display department-level average marks."""
    print("\nDEPARTMENT-WISE AVERAGE")
    department_summary = results.groupby("Department")["Average_Marks"].mean().sort_values(ascending=False)
    print(department_summary.round(2).to_string())


def main():
    try:
        data = load_data()
        results = add_student_results(data)
        print("\nDATASET PREVIEW")
        print(data.head(5).to_string(index=False))
        show_overall_summary(results)
        show_subject_analysis(results)
        show_top_performers(results)
        show_department_analysis(results)

        output_file = "student_analysis_results.csv"
        results.to_csv(output_file, index=False)
        print(f"\nFull results saved to: {output_file}")
    except FileNotFoundError:
        print(f"Error: '{DATA_FILE}' not found. Keep main.py and students.csv in the same folder.")
    except (ValueError, KeyError) as error:
        print(f"Could not process the dataset: {error}")


if __name__ == "__main__":
    main()
