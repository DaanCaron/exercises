from itertools import cycle

class Book:
    def __init__(self, title, isbn):
        if not Book.__is_valid_titel(title):
            raise RuntimeError()
        if not Book.__is_valid_isbn(isbn):
            raise RuntimeError()
        
        self.__title = title
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    
    @staticmethod
    def __is_valid_titel(titel):
        return len(titel) > 0
    
    @staticmethod
    def __is_valid_isbn(isbn):
        digits = [int(char) for char in isbn if "0" <= char <= "9"]
        if len(digits) != 13:
            return False
        weighted_sum = sum(
            digit * weight
            for digit, weight in zip(digits, cycle([1,3]))
        )

        return weighted_sum % 10 == 0
        