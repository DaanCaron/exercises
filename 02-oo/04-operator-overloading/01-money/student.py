class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency
    
    def __add__(self, money_to_add):
        if money_to_add.currency is not self.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount + money_to_add.amount, self.currency)
    
    def __sub__(self, money_to_add):
        if money_to_add.currency is not self.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount - money_to_add.amount, self.currency)
    
    def __mul__(self, factor):
        return Money(self.amount * factor, self.currency)
