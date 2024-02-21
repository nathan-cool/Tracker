class expense:
    def __init__(self, name, category, amount, date):
        """ Initialize attributes"""
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        """Return a string representation of the expense object"""
        return f"expense(name={self.name}, amount={self.amount}, " \
               f"category={self.category}, date={self.date})"