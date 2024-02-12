class expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f"expense(name={self.name}, amount={self.amount}, category={self.category}, date={self.date})"
        
        

