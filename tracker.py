from expense import expense
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Expenses')  
WORKSHEET = SHEET.worksheet('Sheet1')   


def get_expenses():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: €"))
    print(f"You've entered the expense: {expense_name}")
    print(f"Your expensxe amount was: €{expense_amount}")

    expense_categories = [
         "Housing", 
         "Transportation", 
         "Food", 
         "Utilities", 
         "Misc"
     ]
   
    while True: 
        print("Pick a category: ")
    
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")
        
        range_list = f"[1 - {len(expense_categories)}]"
        
        selected_category = int(input(f"Please choose a category {range_list}: ")) - 1
        
        if selected_category in range(len(expense_categories)):
            category = expense_categories[selected_category]
            new_expense = expense(expense_name, category, expense_amount)
            return new_expense
        else: 
            print("🛑 Invalid section, please try again")


def write_expense_to_sheet(expense): 
    print(f"Saving expense: {expense} to Google Sheets")
    WORKSHEET.append_row([expense.name, expense.amount, expense.category])


def read_file_and_summarize():
    all_data = WORKSHEET.get_all_records()
    expenses = []

    for row in all_data:
        expenses.append(expense(row['name'], float(row['amount']), row['category']))

    print(expenses)


def main():
    print(f"💶 Welcome to the Expense App 💶 ") 
    expense = get_expenses()
    write_expense_to_sheet(expense)   

if __name__ == "__main__":
    main()