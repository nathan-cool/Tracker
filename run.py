# libraries
from Expense import expense  # A custom module to manage expense objects
import gspread  # For interacting with Google Sheets
import datetime  # For handling dates
from google.oauth2.service_account import Credentials  # API authentication
import numpy as np  # Handle numerical operations
import pandas as pd
import time   # Time access and conversions
from rich.console import Console  # formatting in the terminal

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
console = Console()


def clear():
    """Clear the console screen to make the app more user-friendly."""
    print('\033c')


def get_expenses():
    """Prompt user for expense details, validate input,
    and return a new expense object."""
    clear()
    while True:
        try:
            expense_name = input("Please enter expense description:")
            
            
            if expense_name.strip():
                break
            
            else:
                clear()
                console.print('Invalid entry. Please enter a description',
                            style="bold red")
        except ValueError:
            clear()
            console.print('Invalid entry. Please enter a description.',
                          style="bold red")
        
    clear()
    while True:
        try:
            expense_amount = float(input("Enter expense amount: €").strip())
            if expense_amount > 0:
                break
            else:
                clear()
                console.print("Invalid entry. Please enter positive values only.",
                              style="bold red")
        except ValueError:
            clear()
            console.print("Invalid entry. Please enter numeric values only.",
                          style="bold red")
    while True:
            expense_date = input("Please use DD-MM-YYYY or press 't' for"
                                 " todays date:").strip()
            if expense_date.lower() in ('t', 'T'):
                expense_date = datetime.datetime.now().date()
                break
            else:
                try:
                    expense_date = datetime.datetime.strptime(
                    expense_date, '%d-%m-%Y').date()
                    break
                except ValueError:
                    clear()
                    console.print("Invalid date format."
                                "Please use DD-MM-YYYY or 't'.", style="bold red")
    clear()
    while True:
            expense_categories = ["Housing", "Transportation", "Food",
                                  "Utilities", "Misc"]
            print("Pick a category: ")

            for i, category_name in enumerate(expense_categories):
                print(f"  {i + 1}. {category_name}")

            range_list = f"[1 - {len(expense_categories)}]"
               
            try:
                selected_category = int(input(f"Please choose a category {range_list}: ")) - 1
                if 0 <= selected_category < len(expense_categories):
                    category = expense_categories[selected_category]
                    new_expense = expense(expense_name, category, expense_amount, expense_date)
                    return new_expense
                else:
                    clear()
                    console.print(f"Invalid selection. Please choose a number between 1 and {len(expense_categories)}.",
                                style="bold red")
            except ValueError:
                clear()
                console.print("Invalid input. Please enter a valid number.", style="bold red")


def write_expense_to_sheet(expense):
    """Save the given expense object to the Google Sheet."""
    clear()
    print(f"Saving expense: {expense} to Google Sheets")
    expense_date_str = expense.date.strftime('%Y-%m-%d')
    try:
        WORKSHEET.append_row(
            [
                expense.name,
                expense.category,
                expense.amount,
                expense_date_str,
            ]
        )
        time.sleep(0.15)
        print("\n")
        console.print("Expense saved", style="green")
    except gspread.exceptions.APIError as e:
        console.print("Error saving expense. Please try again later.",
                      style="bold red")
    except Exception as e:
        console.print(f"An error occurred: {e}", style="bold red")
    print("\n")


def read_file_and_summarize():
    """Fetch expense records from Google Sheet, calculate total,
    and print summary."""
    clear()
    all_data = WORKSHEET.get_all_records()
    expenses = []
    total_expenses = 0.0
    row = 0

    for row in all_data:
        try:
            expense_entry = {
                "DESC": row["name"],
                "AMOUNT": float(row["amount"]),
                "CATEGORY": row["category"],
                "DATE": row["date"]}
            expenses.append(expense_entry)
        except ValueError:
            console.print(f"Error converting amount in row: {row}",
                          style="bold red")

    # Print each expense
    for expense in expenses:
        total_expenses += expense["AMOUNT"]
    pd_total_expenses = pd.DataFrame(expenses)
    print(pd_total_expenses)
    print("----------------------------------------")
    print(f"Total of expenses: €{total_expenses}")
    print("\n")
    budget(total_expenses)
    print("\n")
    input("Press Enter to return to the main menu...\n")
    clear()


def set_budget():
    """Prompts the user to set a new budget and saves it to a file."""
    while True:
        print("To set your new budget, please enter"
              "a numerical value and press enter.")
        print("\n")
        try:
            budget_input = input("Please enter a budget:€").strip()
            budget_value = float(budget_input)

            if budget_value <= 0:
                clear()
                console.print("Invalid input. Please enter a positive number.",
                              style="bold red")
            else:
                np.save("budget.npy", budget_value)
                clear()
                console.print(f"Budget €{budget_input} saved...", style="green")
                break

        except ValueError:
            clear()
            console.print("Invalid input. Please enter a number.\n",
                          style="bold red")
        except Exception as e:
            clear()
            console.print(f"An error occurred: {e}", style="bold red")


def budget(current_spend):
    """Compares the current spend against the saved budget and prints
    a message indicating the status."""
    try:
        budget = np.load("budget.npy")
    except FileNotFoundError:
        console.print("Error, No file found", style="bold red")
        budget = 0.0
    except Exception as e:
        console.print(f"An error occurred: {e}", style="bold red")
        budget = 0.0

    if current_spend > budget:
        console.print(f"The amount exceeds the budget of {budget}",
                      style="red")
    elif current_spend == budget:
        console.print(f"The amount is exactly at the budget limit of {budget}",
                      style="orange")
    else:
        console.print(f"The amount is within the budget of {budget}",
                      style="green")


def main():
    """
    The main function to run the expense application.
    It provides the user with two options:view expenses or create a new
    expense. Handles user input to navigate through the app functionality.
    """
    clear()
    home_screen = [
        "View Expenses",
        "Create New Expense",
        "Set Budget",
        "Exit"
    ]

    while True:
        print("Main Menu For Expense Tracker App")
        print("\n")
        print("Would you like to view past expenses,"
              "create a new expense or set you budget?")
        print("\n")
        print("Pick an option: ")
        print("\n")
        for i, option in enumerate(home_screen):
            print(f"  {i + 1}. {option}")
        print('\n')
        print("Please choose an option between 1 - 4:")
        selected_option = input("Please enter your option here:\n")

        if selected_option == '1':
            read_file_and_summarize()
        elif selected_option == '2':
            new_expense = get_expenses()
            write_expense_to_sheet(new_expense)
        elif selected_option == '3':
            set_budget()
        elif selected_option == '4':
            print('Goodbye')
            break
        else:
            console.print("Error: Invalid input. Please enter a number"
                          " between 1 - 4", style="bold red")


if __name__ == "__main__":

    main()
