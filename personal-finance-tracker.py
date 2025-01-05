import datetime

class FinanceTracker:
    def __init__(self):
        self.transactions = []  # List to store all transactions

    def add_income(self, amount, description):
        """Add an income transaction."""
        transaction = {
            'type': 'Income',
            'amount': amount,
            'description': description,
            'date': datetime.datetime.now()
        }
        self.transactions.append(transaction)
        print("Income added successfully!")

    def add_expense(self, amount, description):
        """Add an expense transaction."""
        transaction = {
            'type': 'Expense',
            'amount': amount,
            'description': description,
            'date': datetime.datetime.now()
        }
        self.transactions.append(transaction)
        print("Expense added successfully!")

    def view_transactions(self):
        """View all transactions."""
        if not self.transactions:
            print("No transactions recorded yet.")
            return
        print("\nTransaction History:")
        for idx, transaction in enumerate(self.transactions, 1):
            print(f"{idx}. {transaction['date'].strftime('%Y-%m-%d %H:%M:%S')} - "
                  f"{transaction['type']}: ${transaction['amount']} ({transaction['description']})")

    def calculate_balance(self):
        """Calculate the current balance."""
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'Income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'Expense')
        return income - expenses


def main():
    tracker = FinanceTracker()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter the income amount: "))
                description = input("Enter a description for this income: ")
                tracker.add_income(amount, description)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")
        elif choice == '2':
            try:
                amount = float(input("Enter the expense amount: "))
                description = input("Enter a description for this expense: ")
                tracker.add_expense(amount, description)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")
        elif choice == '3':
            tracker.view_transactions()
        elif choice == '4':
            balance = tracker.calculate_balance()
            print(f"\nCurrent Balance: ${balance:.2f}")
        elif choice == '5':
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
