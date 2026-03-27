# Student Attendance Record - Project Report

## 1.Introduction:

Attendance is an important in most colleges and schools. For example in VIT Bhopal, there is a minimum requirtment to have at least 75% attendance in your classes otherwise you will be debarred from writing the exams for that subject.

This project aims to solve that issue by making a simple system that calculates current attendance and seeing if the student will meet the minimum requirtments to sit in that class's exam.

---

## 2. Problem Statement:

Many students need to take holidays or leaves due to a family emergency, important family function, health issues or just need a break from the stressful college life and they don't know if missing a few classes will affect their eligibility to sit in their classes exams

The problem addressed in this project is to provide a simple and clear way to:

* calculate attendance percentage
* predict future attendance
* determine whether a student risks falling below 75% attendance

---

## 3. Methodology

The project is divided into two main parts:

1. Dataset Analysis
   A dataset was created to mimic a student's attendance record. Using this data, attendance percentage was calculated and basic statistical measures such as mean, variance, and standard deviation were found.

2. User Input System
   A separate program allows users to input their own attendance details. Based on the input given, the system calculates current attendance and predicts whether the student will be able to meet the required 75% attendance after considering remaining classes.

---

## 4. Implementation

The project was implemented using Python.

* The pandas library was used in the project to read and analyze the dataset.
* Attendance percentage was calculated using mathematical formulas.
* A decision system was implemented to classify students on the basis of their attendance as:

  * "Will not be debarred"
  * "Will be debarred"


The logic also calculates the maximum number of classes a student can miss while still maintaining the attendance needed to appear in the exams

---

## 5. Key Decisions

Some important decisions that were taken during the project:

* A simple rule-based approach was used to keep the system easy to understand and practical.
* The project was divided into two parts (analysis and user input) to clearly separate data processing and real-time usage.
* A clean and minimal dataset was used to avoid unnecessary complexity in the code or the data itself

---

## 6. Challenges Faced

A few challenges were faced during the development of this project:

* Issues while reading the CSV file due to wrong file paths
* Errors caused by mismatched or misread column names
* Understanding how to correctly and effiecently use pandas operations
* Debugging some syntax errors and logic mistakes in the code

These challenges helped me in improving my understanding of Python and data handling.

---

## 7. Results

The system successfully calculates attendance percentage and predicts whether a student will meet the required 75% attendance.

It is able to:

* identify students who can 
* identify students who may be at risk
* provide a clear indication of how many classes can be missed to still appear in the exams

---

## 8. Conclusion

This project offers a straightforward and useful answer to a typical issue that students encounter. It enables students to easily understand their circumstances and make better attendance decisions.

Adding a graphical user interface or incorporating real-time data might enhance the system even more.
---

## 9. What I Learned

This project taught me:
* How to use pandas to work with CSV files
* How to compute statistical measures
* How to construct rational decision-making systems
* The significance of debugging and clean data

My comprehension of fundamental AI ideas and my ability to solve problems have both improved as a result of this research.

