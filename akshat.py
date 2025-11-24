#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     24-11-2025
# Copyright:   (c) HP 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import math

def get_grade_info(marks):
    if marks >= 90:
        return {'grade': 'O (Outstanding)', 'gp': 10}
    elif marks >= 80:
        return {'grade': 'A+ (Excellent)', 'gp': 9}
    elif marks >= 70:
        return {'grade': 'A (Very Good)', 'gp': 8}
    elif marks >= 60:
        return {'grade': 'B+ (Good)', 'gp': 7}
    elif marks >= 50:
        return {'grade': 'B (Above Average)', 'gp': 6}
    elif marks >= 45:
        return {'grade': 'C (Average)', 'gp': 5}
    elif marks >= 40:
        return {'grade': 'P (Pass)', 'gp': 4}
    else:
        return {'grade': 'F (Fail)', 'gp': 0}


def calculate_sgpa(semester_data):
    total_credit_points = 0
    total_credits = 0
    failed_subjects = []

    print(f"\n--- Semester {semester_data['semester']} Results ---")

    for subject in semester_data['subjects']:
        marks = subject['marks']
        credits = subject['credits']
        grade_info = get_grade_info(marks)
        grade_point = grade_info['gp']

        is_pass = grade_point > 0

        credit_points = grade_point * credits
        total_credit_points += credit_points
        total_credits += credits

        status = "PASS" if is_pass else "FAIL"
        print(
            f"  {subject['name']:<30} | Marks: {marks:<3} | Grade: {grade_info['grade']:<20}"
            f" | GP: {grade_point:<2} | Credits: {credits:<2} | Status: {status}"
        )

        if not is_pass:
            failed_subjects.append(subject['name'])

    if total_credits > 0:
        sgpa = total_credit_points / total_credits
        rounded_sgpa = round(sgpa, 2)
    else:
        rounded_sgpa = 0.0

    print(f"\n  Total Credits Attempted: {total_credits}")
    print(f"  Total Credit Points: {total_credit_points}")
    print(f"  SGPA: {rounded_sgpa}")

    if failed_subjects:
        print(f"  *** ACTION REQUIRED: Failed in subjects: {', '.join(failed_subjects)}. Reappearance needed. ***")

    return rounded_sgpa, total_credits, total_credit_points


def calculate_cgpa(semester_results):
    all_credit_points = sum(r['total_credit_points'] for r in semester_results)
    all_credits = sum(r['total_credits'] for r in semester_results)

    if all_credits > 0:
        cgpa = all_credit_points / all_credits
        rounded_cgpa = round(cgpa, 2)
    else:
        rounded_cgpa = 0.0

    print("\n=======================================================")
    print("           CUMULATIVE MARKSHEET SUMMARY                ")
    print("=======================================================")

    print("\nSemester SGPA Breakdown:")
    for result in semester_results:
        print(f"  Semester {result['semester']}: {result['sgpa']}")
    print("-------------------------------------------------------")

    print(f"Total Credits Considered (Across All Semesters): {all_credits}")
    print(f"Total Cumulative Credit Points: {all_credit_points}")
    print(f"Overall CGPA: {rounded_cgpa}")
    print("=======================================================")

    return rounded_cgpa


def get_positive_integer_input(prompt, min_val=1):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_val:
                return value
            else:
                print(f"Error: Enter a value >= {min_val}.")
        except ValueError:
            print("Error: Enter a whole number.")


def get_marks_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Error: Enter a whole number.")


def get_semester_data(num_semesters):
    all_semesters_data = []

    for i in range(1, num_semesters + 1):
        print(f"\n--- SEMESTER {i} ---")
        num_subjects = get_positive_integer_input("Enter number of subjects: ")

        subjects_data = []
        for j in range(1, num_subjects + 1):
            print(f"  - Subject {j} -")
            subject_name = input("    Subject name: ").strip()
            credits = get_positive_integer_input("    Credits: ")
            marks = get_marks_input("    Marks (0–100): ")

            subjects_data.append({
                'name': subject_name,
                'credits': credits,
                'marks': marks
            })

        all_semesters_data.append({
            'semester': i,
            'subjects': subjects_data
        })

    return all_semesters_data


def interactive_marksheet_generator():
    print("=======================================================")
    print("      INTERACTIVE COLLEGE MARKSHEET CALCULATOR         ")
    print("=======================================================")

    student_name = input("Enter Student Name: ").strip()
    student_id = input("Enter Student ID/Roll No: ").strip()

    num_semesters = get_positive_integer_input("Enter number of semesters completed: ")
    semesters_data = get_semester_data(num_semesters)

    print("\n=======================================================")
    print(f"       COLLEGE MARKSHEET REPORT FOR {student_name.upper()}")
    print(f"       Student ID: {student_id.upper()}")
    print("=======================================================")

    all_semester_results = []

    for semester in semesters_data:
        sgpa, total_credits, total_credit_points = calculate_sgpa(semester)
        all_semester_results.append({
            'semester': semester['semester'],
            'sgpa': sgpa,
            'total_credits': total_credits,
            'total_credit_points': total_credit_points
        })

    if all_semester_results:
        calculate_cgpa(all_semester_results)
    else:
        print("No data entered. Cannot calculate CGPA.")


if __name__ == "__main__":
    interactive_marksheet_generator()