class Calculator():

    def __init__(self):
        pass

    @staticmethod
    def add(arg1, arg2):
        return arg1 + arg2

    @staticmethod
    def subtract(arg1, arg2):
        return arg1 - arg2

    @staticmethod
    def multiply(arg1, arg2):
        pass

    @staticmethod
    def divide(arg1, arg2):
        # use //
        # if divisor == 0 return None
        return None if arg2 == 0 else arg1 // arg2

    @staticmethod
    def square(arg1):
        return arg1**2
