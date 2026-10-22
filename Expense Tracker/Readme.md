Personal Expense Tracker
A beginner-friendly Python command-line application for recording daily expenses, reviewing spending, finding the highest expense, and viewing expenses by category.
Features
- Add an expense with a category and amount
- View all recorded expenses
- Calculate total spending
- Find the highest individual expense
- Filter expenses by category
- Calculate the total spent in a selected category
- Handle invalid amount input
- Navigate the application through a simple menu
Technologies Used
- Language: Python
- Editor: Visual Studio Code (VS Code)
Requirements
- Python 3 installed
- Visual Studio Code or another Python-compatible editor
No external Python packages are required.
Getting Started
1. Get the project
If the project is hosted on GitHub, clone it using:
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
Replace the placeholders with your GitHub username and repository name. Alternatively, download the project files and open the folder in VS Code.
2. Run the program
Open the project folder in VS Code. Open the terminal (Terminal → New Terminal) and run:
python personal_expense_tracker.py
If your system uses python3, run:
python3 personal_expense_tracker.py
If your Python file has a different name, replace personal_expense_tracker.py with your actual filename.
How to Use
When the program starts, choose an option from the menu:
1. Add Expense — enter a category and an amount.
2. View All Expenses — display all expenses recorded during the current run.
3. View Total Spent — calculate the sum of all recorded expenses.
4. Find Highest Expense — show the category and amount of the largest expense.
5. View Expenses by Category — list expenses in a selected category and calculate their total.
6. Exit — close the application.
Example
Example expenses:
Category	Amount
Food	₹250
Travel	₹120
Shopping	₹800
Food	₹150
Total	₹1,320


Expected summary:
- Total spent: ₹1,320
- Highest expense: ₹800 (Shopping)
- Food category total: ₹400
Data Structure
Expenses are stored in a list of dictionaries. Each dictionary contains a category and an amount.
expenses = [
    {"category": "Food", "amount": 250},
    {"category": "Travel", "amount": 120},
    {"category": "Shopping", "amount": 800},
    {"category": "Food", "amount": 150}
]
Python Concepts Practiced
- Lists — keep track of multiple expenses
- Dictionaries — store each expense's category and amount
- Functions — organize actions into reusable blocks
- Loops — display expenses and repeat the menu
- Conditional statements — process menu selections
- List comprehensions — filter expenses by category
- Built-in functions — calculate totals and find the highest expense
- Exception handling — handle invalid numeric input
Project Structure
personal-expense-tracker/
├── personal_expense_tracker.py
└── README.md
Limitations
Expenses are stored in memory, so they are cleared when the program exits. The current version does not save expenses to a file or database.
Future Improvements
- Record the date for each expense
- Delete or edit an expense
- Save and load expenses using JSON or CSV
- Set a monthly budget and show remaining balance
- Display category-wise spending summaries
Learning Purpose
This project was created to practise Python fundamentals by building a simple menu-driven command-line application.
Author: Nithya S