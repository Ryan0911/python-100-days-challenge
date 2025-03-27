# pylint: disable=C0114
from utils.art import ArtHelper
class Calculator:
    """Simple calculator class to perform basic arithmetic operations"""    
    def __init__(self):
        self.result = 0
        print(ArtHelper.calculator())

    def add(self, num1, num2):
        """Perform addition of two numbers and return the result
        
        Args:
            num1 (int): First number
            num2 (int): Second number
        
        Returns:
            int: The result of the addition
        """
        self.result = num1 + num2
        return self.result

    def subtract(self, num1, num2):
        """Perform subtraction of two numbers and return the result

        Args:
            num1 (int): First number
            num2 (int): Second number

        Returns:
            int: The result of the subtraction
        """
        self.result = num1 - num2
        return self.result

    def multiply(self, num1, num2):
        """Perform multiplication of two numbers and return the result
        
        Args:
            num1 (int): First number
            num2 (int): Second number
        
        Returns:
            int: The result of the multiplication
        """
        self.result = num1 * num2
        return self.result

    def divide(self, num1, num2):
        """Perform division of two numbers and return the result

        Args:
            num1 (int): First number
            num2 (int): Second number
        
        Returns:
            float: The result of the division
        """
        self.result = num1 / num2
        return self.result

    def reset(self):
        """Reset the calculator result to 0
        
        Returns:
            int: The result of the calculator is reset to 0
        """
        self.result = 0
        return self.result

    def get_result(self):
        """Get the current result of the calculator
        
        Returns:
            int: The current result of the calculator
        """
        return self.result
