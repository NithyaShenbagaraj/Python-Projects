Student Report Card Generator
A beginner-friendly Python application that collects student details and subject marks, calculates the total and average, assigns a grade, and displays a formatted report card in the terminal.
Features
- Accepts a student's ID and name
- Collects marks for multiple subjects
- Stores subject marks in a Python dictionary
- Calculates total marks and average
- Assigns a grade based on the average
- Prints a neatly formatted report card
Technologies Used
- Language: Python
- Editor: Visual Studio Code (VS Code)
Requirements
- Python 3 installed
- Visual Studio Code or another Python-compatible editor
No external Python packages are required.
Getting Started
1. Clone the repository
Replace YOUR-USERNAME and YOUR-REPOSITORY with your GitHub username and repository name.
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
Alternatively, download the repository ZIP file from GitHub and extract it.
2. Open the project in VS Code
Open the project folder in Visual Studio Code. Make sure Report card.py is in the folder.
3. Run the program
Open the VS Code terminal (Terminal → New Terminal) and run:
python "Report card.py"
If your system uses python3, run:
python3 "Report card.py"
Follow the prompts to enter the student ID, name, and marks for each subject.

**Example terminal output:**
Enter student Id: 201
Enter student name: nithii
Enter marks for Language :90
Marks for Language : 90.0
Enter marks for English :70
Marks for English : 70.0
Enter marks for Maths :67
Marks for Maths : 67.0
Enter marks for Science :90
Marks for Science : 90.0
Enter marks for Programming :78
Marks for Programming : 78.0
Total marks: 395.0
Grade: B
===================================
<<<<<<< HEAD
         Student Report Card
===================================
Student ID   : 101
Student Name : nithi
===================================
Subject        : Marks     
Language        56.0      
English         78.0      
Maths           90.0      
Science         78.0      
Programming     90.0      
===================================
Total Marks    : 392.0     
Average        : 78.40     
Grade          : B         
=======
        ** Student Report Card**
===================================
Student ID   : 201
Student Name : nithii
>>>>>>> refs/remotes/origin/main
===================================
**Subject         Marks     
Language        90.0      
English         70.0      
Maths           67.0      
Science         90.0      
Programming     78.0      
Total Marks     395.0     
Average         79.00     
Grade           B         **


Python Concepts Practiced
- Variables and user input — collect student information
- Dictionaries — store subject marks
- Loops — collect and display marks for each subject
- Built-in functions — calculate totals and count subjects
- Conditional statements — assign grades
- F-strings — format the report card output
Project Structure
student-report-card-generator/
├── Report card.py
└── README.md
Future Improvements
- Validate marks to ensure they are between 0 and 100
- Support multiple students in one run
- Save report cards to a file
- Display the student with the highest average
Learning Purpose
This project was created to practise Python fundamentals and build a simple command-line application as a beginner project.
Author: Nithya S
