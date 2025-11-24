# Interactive College Marksheet Calculator

A Python-based interactive CLI tool that lets you calculate SGPA, CGPA, track subject-wise performance, and generate a clean semester-wise marksheet.

This project is perfect for students who want to quickly compute academic performance or build a college-grade calculation system.




 #Features

Interactive input for multiple semesters

SGPA calculation with credit-weighted grading

CGPA calculation from cumulative semesters

Automatic grade assignment based on marks

Fail/pass detection with warnings

Clear summary for each semester and overall performance

Uses a flexible grading rule system





#Grading Criteria

Marks Range	Grade	Grade Points

90–100	O (Outstanding)	10
80–89	A+ (Excellent)	9
70–79	A (Very Good)	8
60–69	B+ (Good)	7
50–59	B (Above Average)	6
45–49	C (Average)	5
40–44	P (Pass)	4
< 40	F (Fail)	0





#How It Works

The system asks for:

Student Name & ID

Number of semesters completed

Number of subjects in each semester

Subject name, credits, and marks


#It then:

Calculates SGPA for each semester

Finds cumulative CGPA

Shows fail subjects (if any)

Prints a complete academic summary





#Running the Program

Make sure you have Python 3.x installed.

Run the script:

python main.py

You will be guided step-by-step through the process.




#Project Structure

 Marksheet-Calculator
  main.py
  README.md



#Implementation Highlights

Modular functions for clarity

Validated inputs to avoid crashes

Uses dictionaries for grade mapping

Clean printing for professional marksheets





 #Example Output (Snippet)

 Semester 1 Results 
Maths                       | Marks: 85  | Grade: A+ (Excellent) | GP: 9 | Credits: 4 | Status: PASS
Physics                     | Marks: 42  | Grade: P (Pass)       | GP: 4 | Credits: 3 | Status: PASS

SGPA: 7.14




