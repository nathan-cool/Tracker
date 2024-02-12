# libraries
from expense import expense  # Presumably a custom module to manage expense objects
import gspread  # For interacting with Google Sheets
import datetime  # For handling dates
from google.oauth2.service_account import Credentials  # For Google Sheets API authentication
import numpy as np

# Define the scope needed for Google Sheets and Drive API access
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Authenticate using service account credentials
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the specific Google Sheet and worksheet
SHEET = GSPREAD_CLIENT.open("Expenses")
WORKSHEET = SHEET.worksheet("Sheet1")

def get_expenses():
    """
    Prompts user to input expense details, validates the input, and returns a new expense object.
    The function will ask for the expense's name, amount, date, and category.
    It supports entering 'T' for the current date and enforces a valid date format and category selection.
    """
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: €"))
    expense_date = input("please enter date of expense: ")
    while True:
        if expense_date.lower() == 't':
           expense_date = datetime.datetime.now().date()
        else:
            try:
                expense_date = datetime.datetime.strptime(expense_date, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD or 'T'.")
        break
    
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
    """
    Saves the given expense object to the Google Sheet.
    It formats the date to 'YYYY-MM-DD' before appending the expense data as a new row in the worksheet.
    """
    print(f"Saving expense: {expense} to Google Sheets")
    expense_date_str = expense.date.strftime('%Y-%m-%d')
    WORKSHEET.append_row([expense.name, expense.amount, expense.category, expense_date_str])

def read_file_and_summarize():
    """
    Fetches all expense records from the Google Sheet, calculates the total expenses,
    and prints each expense and the total amount spent.
    Handles potential ValueError when converting the expense amount to float.
    """
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
    budget(total_expenses)

def clear():
    """
    Clears the console screen to make the app more user-friendly.
    It uses an escape sequence to clear the console.
    """
    print('\033c')

def main():
    """
    The main function to run the expense application.
    It provides the user with two options: view expenses or create a new expense.
    Handles user input to navigate through the app functionality.
    """
    set_budget ()
    clear()
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
            
def set_budget ():
    budget_input = input("Please enter a budget")
    
    set_budget = "budget.csv"
    
    with open (set_budget, 'w') as file:
        file.write(str(budget_input))
   
    

def budget(current_spend):
    set_budget = "budget.csv"
    
    with open (set_budget, 'r') as file:
        last_saved = file.read()
        if float(current_spend > last_saved):
            print("Gone over budget")
        else:
            return 

main()
