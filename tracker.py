from expense import expense
import emoji 


def main():
    print(f"💶 Welcome to the Expense App 💶 ")

    expense_file_path = "expenses.csv"
    # Get input for expense
    expense = get_expenses()
    # Write expense to file 
    write_expense_to_file(expense, expense_file_path)
    # Read file and summarize 
    read_file_and_summarize(expense_file_path)
    



def get_expenses():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: €"))
    print(f"You've entered the expense: {expense_name}")
    print(f"Your expense amount was: €{expense_amount}")
     
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

        # NEED TO FIX FOR STR INPUTS ON THE CATEGORY USER SELECTS 
     
   
def write_expense_to_file(expense, expense_file_path):
    print(f"Saving expense: {expense} to {expense_file_path}")
    with open (expense_file_path, "a") as file:
        file.write(f"{expense.name},{expense.amount},{expense.category}\n")
    
    
    
    
def read_file_and_summarize(expense_file_path):
    expenses = []
    with open (expense_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")

            line_expenses = expense(expense_name, float(expense_amount), expense_category)
            expenses.append(line_expenses)
            print(line_expenses)
        print(expenses)
            
            
            


if __name__ == "__main__":
    main()