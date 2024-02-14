# libraries
from expense import expense  # A custom module to manage expense objects
import gspread  # For interacting with Google Sheets
import datetime  # For handling dates
from google.oauth2.service_account import Credentials  # For Google Sheets API authentication
import numpy as np
import pandas as pd

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
    clear()
    expense_name = input("Enter expense name: ")
        
    while True:
        try:
            print('Please enter numeric values only')
            expense_amount = float(input("Enter expense amount: €"))   
            break
        except ValueError:
            print('Invalid entry. Please enter numeric values only. \n ')
    clear()
    while True:
            try:
                expense_date = input("Please use DD-MM-YYYY or press 't' for todays date: ")
                if expense_date.lower() in ('t' , 'T'):
                    expense_date = datetime.datetime.now().date()
                else:
                    expense_date = datetime.datetime.strptime(expense_date, '%d-%m-%Y').date()
                break
            except ValueError:
                print("Invalid date format. Please use DD-MM-YYYY or 't'. \n ")
    clear()                   
    while True:
            try:
                expense_categories = ["Housing", "Transportation", "Food", "Utilities", "Misc"]
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
                    print(f"Invalid selection. Please choose a number between 1 and {len(expense_categories)}.\n")
            except ValueError:
                clear()  
                print("Invalid input. Please enter a number.\n")
            
    

def write_expense_to_sheet(expense):
    clear()
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
        except ValueError:
            print(f"Error converting amount in row: {row}")

    # Print each expense
    for expense in expenses:
        total_expenses += expense_entry["amount"]
    
    
    pd_total_expenses = pd.DataFrame(expenses)
    print(pd_total_expenses)
    print("----------------------------------------")
    print(f"Total of expenses: €{total_expenses}")
    

def clear():
    """
    Clears the console screen to make the app more user-friendly.
    It uses an escape sequence to clear the console.
    """
    print('\033c')
            
def set_budget ():
    budget_input = input("Please enter a budget:€")
    
    np.save("budget.npy", float(budget_input))
   
    

def budget(current_spend):
  
    budget = np.load("budget.npy")
        
    if current_spend > budget:
            print("The amount exceeds the budget.")
    elif current_spend == budget:
            print("The amount is exactly at the budget limit.")
    else:
            print("The amount is within the budget.")
    print(f"€{budget}")
    
    clear()  

def main():
    """
    The main function to run the expense application.
    It provides the user with two options: view expenses or create a new expense.
    Handles user input to navigate through the app functionality.
    """
    clear()
    home_screen = [
        "View expenses",
        "Create new expense",
        "Set budget",
        "Exit"
    ]

    print("💶 Welcome to the Expense App 💶")
    print("💶 Would you like to view past expenses, create a new expense or set you budget? 💶")

    while True:
            print("Pick an option: ")
            for i, option in enumerate(home_screen):
                print(f"  {i + 1}. {option}")
            
            selected_option = input("Please choose an option [1][2][3][4]: ").strip()
            
            if selected_option == '1':
                read_file_and_summarize()
                break
            elif selected_option == '2':
                new_expense = get_expenses()
                write_expense_to_sheet(new_expense)
            elif selected_option == '3':
                set_budget ()
            elif selected_option == '4':
                print('Goodbye')
                break
            else:
               print("Error: Invalid input. Please enter a number between 1 and 3")    
    

main()


    