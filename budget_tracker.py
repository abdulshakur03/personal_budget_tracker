from datetime import date

transactions = []
current_day = date.today()


def main():
    start()


def start():
    while True:
        print("===== BUDGET TRACKER =====")

        print(
            "[1] Add Income\n[2] Add Expense\n[3] View All\n[4] Summary\n[5] By Category\n[6] Exit"
        )
        option = user_prompt("an option ")
        if option == "1":
            add_income()
        elif option == "2":
            add_expense()
        elif option == "6":
            return
        else:
            print("not a valid option")

        print(transactions)


def add_income():
    source = user_prompt("source ")
    income_amount = get_amount()

    income_details = {
        "type": "income",
        "source": source,
        "income_amount": income_amount,
        "income_date": current_day,
    }

    transactions.append(income_details)
    # print(transactions)


def add_expense():
    expense_details = {
        "type": "expense",
        "category": user_prompt("category "),
        "description": user_prompt("description "),
        "expense_amount": get_amount(),
        "expense_date": current_day,
    }

    transactions.append(expense_details)
    # print(transactions)


def get_amount():
    while True:
        try:
            amount = int(user_prompt("amount "))
            break
        except ValueError:
            print("Not a valid Number")
    return amount


def user_prompt(value):
    return input(f"Enter {value}")


# add_income()


if __name__ == "__main__":
    main()
