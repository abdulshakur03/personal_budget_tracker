import json
from datetime import date

current_day = date.today().isoformat()
try:
    with open("transaction.json", "r") as f:
        transactions = json.load(f)

except (FileNotFoundError, json.JSONDecodeError):
    transactions = []


def main():

    start()


def start():
    while True:
        print()
        print("===== BUDGET TRACKER =====")

        print(
            "[1] Add Income\n[2] Add Expense\n[3] View All Transactions\n[4] View Summary\n[5] View Expense by Category\n[6] Delete\n[7] Exit"
        )
        print()
        option = user_prompt("an option")
        print()

        if option == "1":
            add_income()
        elif option == "2":
            add_expense()
        elif option == "3":
            view_all_transaction(transactions)
        elif option == "4":
            print("==========FINANCIAL SUMMARY==========\n")
            print()
            summary, _ = view_summary(transactions)
            print(summary)
            print()
        elif option == "5":
            _, total_expense = view_summary(transactions)
            print("==========SPENDING BY CATEGORY==========\n")
            print()
            view_category(transactions, total_expense)
            print()
        elif option == "6":
            delete_expense(transactions)

        elif option == "7":
            print("Goodbye!, Always remember to spend wisely\n\n-MAO")
            break
        else:
            print("Not a valid option, Please choose [1] - [6].\n")
        with open("transaction.json", "w") as f:
            json.dump(transactions, f, indent=4)


def add_income():
    income_item = {
        "type": "income",
        "source": user_prompt("source"),
        "amount": get_amount(),
        "date": current_day,
    }

    transactions.append(income_item)


def add_expense():
    expense_item = {
        "type": "expense",
        "category": user_prompt("category"),
        "description": user_prompt("description"),
        "amount": get_amount(),
        "date": current_day,
    }

    transactions.append(expense_item)


def delete_expense(expenses):
    if not expenses:
        print("Nothing to delete")
        print()
    else:
        view_all_transaction(expenses)
        prompt = int(validate_user_input("a number to delete"))
        print()
        while len(expenses) < prompt:
            print("Select a valid number to delete\n")
            prompt = int(validate_user_input("a number to delete"))
            print()
        expenses.pop(prompt - 1)
        print("Expense Deleted")


def view_all_transaction(details):
    num = 1
    print("==========Recent Transactions==========")
    print()
    if len(details) == 0:
        print("No recent Transactions")
        print()

    for detail in details:
        print(f"------------[{num}]---------------")
        for key, value in detail.items():
            if key == "amount":
                print(f"{key:<20}: {value:,.2f}")
            else:
                print(f"{key:<20}: {value}")
        print("=======================================")
        print()
        num += 1


def view_summary(items):
    total_income = 0
    total_expense = 0
    for item in items:
        if item["type"] == "income":
            total_income += item["amount"]
        elif item["type"] == "expense":
            total_expense += item["amount"]
    net_balance = total_income - total_expense

    return (
        f"{'Total Income:':<20}₦ {total_income:,.2f}\n{'Total Expense:':<20}₦ {total_expense:,.2f}\n{'Net Balance:':<20}₦ {net_balance:,.2f}",
        total_expense,
    )


def view_category(items, total_expense):
    if total_expense == 0:
        print("No expenses recorded yet.")
        print()
        return
    category_total = {}
    for item in items:
        if item["type"] == "expense":
            cat = item["category"].title()
            amt = item["amount"]
            if cat in category_total:
                category_total[cat] += amt
            else:
                category_total[cat] = amt
    for cat_name, cat_amt in category_total.items():
        print(
            f"{cat_name:<20} ₦ {cat_amt:,.2f} ({(cat_amt * 100)/total_expense:,.2f}%)"
        )


def get_amount():
    while True:
        try:
            amount = float(user_prompt("amount"))
            break
        except ValueError:
            print("Not a valid Number")
    return amount


def validate_user_input(text):
    while True:
        try:
            return int(user_prompt(text))
        except ValueError:
            print("Not a valid Number")


def user_prompt(value):
    return input(f"Enter {value}: ")


if __name__ == "__main__":
    main()
