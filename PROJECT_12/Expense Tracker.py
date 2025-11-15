import csv
import os

FILE_NAME = "expenses.csv"

# Initialize CSV file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Category", "Note"])

def add_transaction(trans_type, amount, category, note):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([trans_type, amount, category, note])

def view_summary():
    total_income = 0
    total_expense = 0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["Amount"])
            if row["Type"] == "Income":
                total_income += amount
            else:
                total_expense += amount

    print("\n💰 Summary:")
    print(f"Income: ₹{total_income}")
    print(f"Expenses: ₹{total_expense}")
    print(f"Balance: ₹{total_income - total_expense}")

while True:
    print("\n📒 Expense Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        amt = float(input("Enter income amount: ₹"))
        cat = input("Category: ")
        note = input("Note (optional): ")
        add_transaction("Income", amt, cat, note)
    elif choice == '2':
        amt = float(input("Enter expense amount: ₹"))
        cat = input("Category: ")
        note = input("Note (optional): ")
        add_transaction("Expense", amt, cat, note)
    elif choice == '3':
        view_summary()
    elif choice == '4':
        break
    else:
        print("❌ Invalid choice.")