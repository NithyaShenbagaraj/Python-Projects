
# Personal Expense Tracker

expenses = []


# Function to add an expense
def add_expense():
    category = input("Enter expense category: ").strip()

    try:
        amount = float(input("Enter expense amount: "))

        if not category:
            print("Category cannot be empty.")
        elif amount <= 0:
            print("Amount must be greater than zero.")
        else:
            expense = {
                "category": category.title(),
                "amount": amount
            }

            expenses.append(expense)
            print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n-------- ALL EXPENSES --------")
    print(f"{'Category':<20}{'Amount':>12}")
    print("-" * 32)

    for expense in expenses:
        print(
            f"{expense['category']:<20}"
            f"Rs. {expense['amount']:>8.2f}"
        )

    print("-" * 32)


# Function to calculate total spending
def calculate_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: Rs. {total:.2f}")


# Function to find the highest expense
def highest_expense():
    if not expenses:
        print("No expenses recorded yet.")
        return

    highest = max(expenses, key=lambda expense: expense["amount"])

    print(f"Highest expense category: {highest['category']}")
    print(f"Highest expense amount: Rs. {highest['amount']:.2f}")


# Function to view expenses by category
def view_by_category():
    if not expenses:
        print("No expenses recorded yet.")
        return

    category = input("Enter category to search: ").strip().casefold()

    filtered_expenses = [
        expense for expense in expenses
        if expense["category"].casefold() == category
    ]

    if not filtered_expenses:
        print("No expenses found for this category.")
        return

    print(f"\nExpenses in category: {category.title()}")

    for expense in filtered_expenses:
        print(f"Rs. {expense['amount']:.2f}")

    category_total = sum(
        expense["amount"] for expense in filtered_expenses
    )
    print(f"Category total: Rs. {category_total:.2f}")


# Main menu
while True:
    print("\n====== PERSONAL EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spent")
    print("4. Find Highest Expense")
    print("5. View Expenses by Category")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        highest_expense()
    elif choice == "5":
        view_by_category()
    elif choice == "6":
        print("Thank you for using the Expense Tracker!")
        break
    else:
        print("Invalid choice. Please select 1-6.")
