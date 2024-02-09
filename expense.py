class expense:
    def __init__(self, name, category, amount, date) -> None:
        self.name = name 
        self.category = category 
        self.amount = amount 
        self.date = date 
        
    def __repr__(self):
        return f"|Expense: {self.name}, {self.amount}, {self.category}|"
        
        

