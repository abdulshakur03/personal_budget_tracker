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
        while True:
            try:
                if option == "1":
                    add_income()
                elif option == "2":
                    add_expense()
                elif option == "3":
                    view_all_transaction(transactions)
                elif option == "4":
                    view_summary(transactions)
                elif option == "6":
                    return
                else:
                    print("not a valid option")
                break
            except ValueError:
                print("Enter an option from [1] - [6]")


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


def view_all_transaction(details):
    print("==========Recent Transactions==========")
    print()
    for detail in details:
        for key, value in detail.items():
            print(f"{key:<20}: {value}")
            print()
        print("=======================================")
        print()


def view_summary(details):
    print("==========FINANCIAL SUMMARY==========")
    print()
    total_income = 0
    total_expense = 0
    for detail in details:
        for key in detail.keys():
            if key == "income_amount":
                total_income += detail["income_amount"]
            elif key == "expense_amount":
                total_expense += detail["expense_amount"]
    net_balance = total_income - total_expense

    print(f"{'Total Income:':<20} ₦ {total_income}")
    print(f"{'Total Expense:':<20}  ₦ {total_expense}")
    print(f"{'Net Balance:':<20}  ₦ {net_balance}")
    print()

def view_category(details):
    

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


if __name__ == "__main__":
    main()
