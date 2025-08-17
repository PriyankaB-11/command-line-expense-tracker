import os
from datetime import datetime
import csv 

csv_file = "expenses.csv"

def add_expense():
    print("--- Add New Expense ---")
    description = input("Enter a brief description of the expense: ")
    category = input("Enter the expense category(e.g., Food,Transport): ")
    while True:
        try:
            amount= float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    date = datetime.now().strftime("%Y-%m-%d")
    with open(csv_file , 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date,description,category,amount])
    print(f"Successfully recorded expense:{description}")

def view_expenses():
    print("--- All Expenses ---")
    try:
        with open(csv_file , 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            expenses = list(reader)
        if not expenses:
            print("No expenses recorded yet.")
            return
        print(f"{header[0]:<12} | {header[1]:<30} | {header[2]:<15} | {header[3]:>10}")
        print("-"*75)
        for expense in expenses:
            date , description , category , amount = expense
            print(f"{date:<12} | {description:<30} | {category:<15} | {float(amount):>10.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet")

def main():
    if not os.path.exists(csv_file):
        with open(csv_file , 'w' , newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Description","Category","Amount"])
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Exit")
        choice = input("Enter your choice(1-3): ")
        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()