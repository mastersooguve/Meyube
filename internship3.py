import csv
import os
import datetime

class Expense:
    def __init__(self, amount, description, category):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = datetime.date.today()

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_monthly_summary(self):
        current_month = datetime.date.today().month
        monthly_expenses = [expense for expense in self.expenses if expense.date.month == current_month]
        total_spent = sum(expense.amount for expense in monthly_expenses)
        return total_spent, monthly_expenses

    def get_category_summary(self, category):
        category_expenses = [expense for expense in self.expenses if expense.category == category]
        total_spent = sum(expense.amount for expense in category_expenses)
        return total_spent, category_expenses

def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Monthly Summary")
    print("3. View Category-wise Summary")
    print("4. Exit")

def get_user_input(prompt):
    return input(prompt)

def save_expenses(expenses):
    with open("expenses.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Description", "Category", "Date"])
        for expense in expenses:
            writer.writerow([expense.amount, expense.description, expense.category, expense.date])

def load_expenses():
    expenses = []
    if os.path.exists("expenses.csv"):
        with open("expenses.csv", "r", newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                amount, description, category, date = row
                expenses.append(Expense(float(amount), description, category))
    return expenses

def main():
    tracker = ExpenseTracker()
    tracker.expenses = load_expenses()

    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            amount = float(get_user_input("Enter the amount spent: "))
            description = get_user_input("Enter a brief description: ")
            category = get_user_input("Enter the category: ")
            expense = Expense(amount, description, category)
            tracker.add_expense(expense)
            save_expenses(tracker.expenses)
            print("Expense added successfully!")
        elif choice == "2":
            total_monthly, monthly_expenses = tracker.get_monthly_summary()
            print("\nTotal spent this month:", total_monthly)
            print("Monthly expenses:")
            for expense in monthly_expenses:
                print(expense.date, "-", expense.description, "-", expense.amount)
        elif choice == "3":
            category = get_user_input("Enter the category to view summary: ")
            total_category, category_expenses = tracker.get_category_summary(category)
            print("\nTotal spent on", category + ":", total_category)
            print(category + " expenses:")
            for expense in category_expenses:
                print(expense.date, "-", expense.description, "-", expense.amount)
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
