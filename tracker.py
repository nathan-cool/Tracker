from expense import expense
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Expenses")
WORKSHEET = SHEET.worksheet("Sheet1")


def get_expenses():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: €"))
    expense_date = input("please enter date of expense")
    print(f"You've entered the expense: {expense_name}")
    print(f"Your expensxe amount was: €{expense_amount}")

    expense_categories = ["Housing", "Transportation", "Food", "Utilities", "Misc"]

    while True:
        print("Pick a category: ")

        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        range_list = f"[1 - {len(expense_categories)}]"

        selected_category = int(input(f"Please choose a category {range_list}: ")) - 1

        if selected_category in range(len(expense_categories)):
            category = expense_categories[selected_category]
            new_expense = expense(expense_name, category, expense_amount, expense_date)
            return new_expense
        else:
            print("🛑 Invalid section, please try again")


def write_expense_to_sheet(expense):
    print(f"Saving expense: {expense} to Google Sheets")
    WORKSHEET.append_row([expense.name, expense.amount, expense.category, expense.date])


def read_file_and_summarize():
    all_data = WORKSHEET.get_all_records()
    expenses = []
    total_expenses = 0.0

    for row in all_data:
        try:
            expense_entry = {
                "name": row["name"],
                "amount": float(row["amount"]),
                "category": row["category"],
                "date": row["date"],
            }
            expenses.append(expense_entry)
            total_expenses += expense_entry["amount"]
        except ValueError:
            print(f"Error converting amount in row: {row}")

    # Print each expense
    for expense in expenses:
        print(expense)
    print("Total Expenses:", total_expenses)


def home_screen_options():
    home_screen = [
        "View expenses",
        "Create new expense",
    ]

    print("💶 Welcome to the Expense App 💶")
    print("💶 Would you like to view past expenses or create a new expense? 💶")

    while True:
        print("Pick an option: ")
        for i, option in enumerate(home_screen):
            print(f"  {i + 1}. {option}")

        selected_option = int(input("Please choose an option (1 or 2): "))

        if selected_option == 1:
            read_file_and_summarize()
            break
        elif selected_option == 2:
            new_expense = get_expenses()
            write_expense_to_sheet(new_expense)
            break
        else:
            print("🛑 Invalid selection, please try again.")


def main():
    home_screen_options()


if __name__ == "__main__":
    main()
