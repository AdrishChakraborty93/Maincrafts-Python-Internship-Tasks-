import csv
import os
def add_expense(desc, amount):
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])
    print("Expense added successfully!")
def view_expenses():
    if not os.path.exists("expenses.csv"):
        print("No expenses recorded yet.")
        return
    print("\n----- All Expenses -----")
    with open("expenses.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"Item: {row[0]}, Amount: ₹{row[1]}")
def total_expenses():
    if not os.path.exists("expenses.csv"):
        print("Total expenses: ₹0")
        return
    total = 0
    with open("expenses.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            total += float(row[1])
    print(f"Total expenses: ₹{total:.2f}")
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spent")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        desc = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        add_expense(desc, amount)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
