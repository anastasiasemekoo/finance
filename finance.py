import csv
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

# File path for the data
data_file = "finance_data.csv"


def add_transaction(date, category, transaction_type, amount):
    """Add a new transaction to the file."""
    with open(data_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, transaction_type, amount])


def view_transactions():
    """Display all transactions with line numbers."""
    with open(data_file, mode="r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader, 1):
            print(f"{i}. {row}")


def edit_transaction(line_number, date, category, transaction_type, amount):
    """Edit an existing transaction."""
    transactions = []
    with open(data_file, mode="r") as file:
        reader = csv.reader(file)
        transactions = list(reader)

    if 0 < line_number <= len(transactions):
        transactions[line_number - 1] = [date, category, transaction_type, amount]
        with open(data_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(transactions)
    else:
        print("Invalid line number.")


def delete_transaction(line_number):
    """Delete an existing transaction."""
    transactions = []
    with open(data_file, mode="r") as file:
        reader = csv.reader(file)
        transactions = list(reader)

    if 0 < line_number <= len(transactions):
        transactions.pop(line_number - 1)
        with open(data_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(transactions)
    else:
        print("Invalid line number.")


def plot_expenses():
    """Display a graph of expenses by category."""
    expenses = {}
    with open(data_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            category, transaction_type, amount = row[1], row[2], float(row[3])
            if transaction_type == "Expense":
                expenses[category] = expenses.get(category, 0) + amount

    categories = list(expenses.keys())
    amounts = list(expenses.values())

    plt.bar(categories, amounts)
    plt.xlabel("Categories")
    plt.ylabel("Amount")
    plt.title("Expenses by Category")
    plt.show()


def validate_input(input_str, input_type):
    """Validate user input."""
    if input_type == "date":
        try:
            datetime.strptime(input_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    elif input_type == "amount":
        try:
            float(input_str)
            return True
        except ValueError:
            return False
    return True


def compare_income_expense():
    """Compare the current month's overall income and expenses with the previous month."""
    current_month = datetime.now().month
    previous_month = current_month - 1 if current_month > 1 else 12
    current_year = datetime.now().year
    previous_year = current_year if current_month > 1 else current_year - 1

    monthly_data = {
        "current_month": {"Income": 0, "Expense": 0},
        "previous_month": {"Income": 0, "Expense": 0},
    }

    with open(data_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            date, _, transaction_type, amount = row
            transaction_date = datetime.strptime(date, "%Y-%m-%d")
            amount = float(amount)

            if (
                transaction_date.month == current_month
                and transaction_date.year == current_year
            ):
                monthly_data["current_month"][transaction_type] += amount
            elif (
                transaction_date.month == previous_month
                and transaction_date.year == previous_year
            ):
                monthly_data["previous_month"][transaction_type] += amount

    print(
        f"Current Month (Income - Expense): {monthly_data['current_month']['Income']} - {monthly_data['current_month']['Expense']}"
    )
    print(
        f"Previous Month (Income - Expense): {monthly_data['previous_month']['Income']} - {monthly_data['previous_month']['Expense']}"
    )


def main():
    while True:
        print("\nPersonal Finance Manager")
        print("1. Add Transaction")
        print("2. Show Transactions")
        print("3. Show Expense Graph")
        print("4. Edit Transaction")
        print("5. Delete Transaction")
        print("6. Compare Current and Previous Month")
        print("7. Exit")
        choice = input("Choose an action: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            while not validate_input(date, "date"):
                date = input("Invalid format. Please enter date (YYYY-MM-DD): ")

            category = input("Enter category: ")
            transaction_type = input("Type (Income/Expense): ")
            amount = input("Enter amount: ")
            while not validate_input(amount, "amount"):
                amount = input("Invalid amount. Please enter a valid number: ")

            add_transaction(date, category, transaction_type, amount)
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            plot_expenses()
        elif choice == "4":
            view_transactions()
            line = int(input("Enter the line number of the transaction to edit: "))
            date = input("Enter new date (YYYY-MM-DD): ")
            while not validate_input(date, "date"):
                date = input("Invalid format. Please enter date (YYYY-MM-DD): ")

            category = input("Enter new category: ")
            transaction_type = input("New type (Income/Expense): ")
            amount = input("Enter new amount: ")
            while not validate_input(amount, "amount"):
                amount = input("Invalid amount. Please enter a valid number: ")

            edit_transaction(line, date, category, transaction_type, amount)
        elif choice == "5":
            view_transactions()
            line = int(input("Enter the line number of the transaction to delete: "))
            delete_transaction(line)
        elif choice == "6":
            compare_income_expense()
        elif choice == "7":
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
