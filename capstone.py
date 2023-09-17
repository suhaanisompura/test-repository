class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.income = 0

    def add_expense(self, category, amount, description, date):
        self.expenses.append({
            'category': category,
            'amount': amount,
            'description': description,
            'date': date
        })

    def add_income(self, amount):
        self.income += amount

    def calculate_balance(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        balance = self.income - total_expenses
        return balance

    def view_expenses(self, category=None, start_date=None, end_date=None):
        filtered_expenses = self.expenses
        if category:
            filtered_expenses = [expense for expense in filtered_expenses if expense['category'] == category]
        if start_date:
            filtered_expenses = [expense for expense in filtered_expenses if expense['date'] >= start_date]
        if end_date:
            filtered_expenses = [expense for expense in filtered_expenses if expense['date'] <= end_date]

        total = sum(expense['amount'] for expense in filtered_expenses)
        
        print("Category\tAmount\tDescription\tDate")
        print("-----------------------------------------------")
        for expense in filtered_expenses:
            print(f"{expense['category']}\t{expense['amount']}\t{expense['description']}\t{expense['date']}")
        print("-----------------------------------------------")
        print(f"Total Expenses\t{total}")
        print(f"Income\t{self.income}")
        print(f"Balance\t{self.calculate_balance()}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            date = input("Enter expense date (YYYY-MM-DD): ")
            tracker.add_expense(category, amount, description, date)
            print("Expense added successfully!")

        elif choice == "2":
            income = float(input("Enter income amount: "))
            tracker.add_income(income)
            print("Income added successfully,working hard i see!")

        elif choice == "3":
            category = input("Enter category to filter (leave empty for all): ")
            start_date = input("Enter start date (leave empty for all): ")
            end_date = input("Enter end date (leave empty for all): ")
            tracker.view_expenses(category, start_date, end_date)

        elif choice == "4":
            print("Exiting Expense Tracker.Spend wisely as money doesnt grow on trees and you work hard!")
            break

        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4).")


if __name__ == "__main__":
    main()
