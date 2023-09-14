class Expense:
    def __init__(self, description, amount, category, date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"Description: {self.description}, Amount: ₹{self.amount}, Category: {self.category}, Date: {self.date}"


class Category:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)


class User:
    def __init__(self, username):
        self.username = username
        self.wallet = 0
        self.categories = {}

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = Category(category_name)
        else:
            print(f"Category '{category_name}' already exists.")

    def add_expense(self, category_name, expense):
        if category_name in self.categories:
            category = self.categories[category_name]
            category.add_expense(expense)
            self.wallet -= expense.amount
            print(f"Expense added to '{category_name}': {expense.description}")
        else:
            print(f"Category '{category_name}' does not exist.")

    def view_balance(self):
        return f"Current Balance for {self.username}: ₹{self.wallet}"

    def view_categories(self):
        return "\n".join(self.categories.keys())

    def view_expenses(self, category_name=None):
        if category_name:
            if category_name in self.categories:
                return "\n".join([str(expense) for expense in self.categories[category_name].expenses])
            else:
                return f"Category '{category_name}' does not exist."
        else:
            all_expenses = []
            for category in self.categories.values():
                all_expenses.extend(category.expenses)
            return "\n".join([str(expense) for expense in all_expenses])


def main():
    username = input("Enter your username: ")
    user = User(username)

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Category")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Categories")
        print("5. View Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category_name = input("Enter category name: ")
            user.add_category(category_name)
        elif choice == '2':
            category_name = input("Enter category name: ")
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: ₹"))
            date = input("Enter expense date (yyyy-mm-dd): ")
            expense = Expense(description, amount, category_name, date)
            user.add_expense(category_name, expense)
        elif choice == '3':
            print(user.view_balance())
        elif choice == '4':
            print("Categories:")
            print(user.view_categories())
        elif choice == '5':
            category_name = input("Enter category name (leave blank to view all expenses): ")
            print("Expenses:")
            print(user.view_expenses(category_name))
        elif choice == '6':
            print("Exiting Expense Tracker.Spend wisely as money doesnt grow on trees and you work hard!")
            break
        else:
            print("oops something went wrong! try again.psst make sure to pick a number between 1/2/3/4/5/6")


if __name__ == "__main__":
    main()
