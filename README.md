Command-Line Expense Tracker

This project is a simple but powerful command-line application built with Python for tracking daily expenses.
It allows users to add new expenses with a description, category, and amount, and view a formatted list of all their past entries.
The application is designed for users who prefer a minimalist, keyboard-driven interface and serves as an excellent beginner project for demonstrating core Python skills.

All data is persistently stored in a local expenses.csv file, ensuring that records are not lost between sessions.
The application is built with clean, modular code, making it easy to understand and extend.

Features--
Add New Expenses: Interactively prompts the user for expense details (description, category, amount).

View All Expenses: Displays a well-formatted table of all recorded expenses, including date, description, category, and amount.

Persistent Storage: Automatically saves all entries to a expenses.csv file and loads them on startup.

Input Validation: Prevents the application from crashing by validating that the expense amount is a valid number.

User-Friendly CLI: A continuous menu loop provides a simple and intuitive command-line interface.

Technologies Used--
Programming Language: Python 3

Standard Library Modules:

csv: For reading from and writing to the CSV data file.

os: To check for the existence of the data file on startup.

datetime: To automatically generate a timestamp for each new expense.
