def main():
    print(f" 🥳 Running Expense App")
    # Get input for expense
    get_expenses()
    # Write expense to file 
    write_expense_to_file()
    # Read file and summarize 
    read_file_and_summarize()
    



def get_expenses():
    print(f" 🫡 Running get expense function")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered the expense {expense_name}")
    print(f"Your expense amount was €{expense_amount}")
     
    expense_categories = [
         "🏠 Housing", 
         "🚙 Transportation", 
         "🍔 Food", 
         "🛠️ Utilities", 
         "💎 Misc"
     ]
   
    while True: 
        print("Pick a category: ")
    
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")
        
        range_list = f"[1 - {len(expense_categories)}]"
        
        selected_category = int(input(f"Please choose a category {range_list}"))
        
        if selected_category <= len(expense_categories):
            
            break
        
        # NEED TO FIX FOR STR INPUTS ON THE CATEGORY USER SELECTES 
     
   
def write_expense_to_file():
    print(f" 😱 Running get write to file function")
    
    
    
def read_file_and_summarize():
    print(f" 🫥 Running get summarize function")
    
    

if __name__ == "__main__":
    main()