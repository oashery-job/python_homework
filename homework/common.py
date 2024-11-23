from abc import ABC, abstractmethod
from logger import log_function
import logging


class AbstractMathOperation(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        pass


@log_function
class Addition(AbstractMathOperation):
    def execute(self, num1, num2):
        return str(num1 + num2)


@log_function
class Subtraction(AbstractMathOperation):
    def execute(self, num1, num2):
        return str(num1 - num2)


@log_function
class Multiplication(AbstractMathOperation):
    def execute(self, num1, num2):
        return str(num1 * num2)


@log_function
class Division(AbstractMathOperation):
    def execute(self, num1, num2):
        try:
            result = num1 / num2
            return str(int(result)) if result == int(result) else f"{result:.2f}"
        except ZeroDivisionError:
            logging.error("Cannot divide by zero")
            return "Error: Division by zero"


ARITHMETIC_OPERATIONS = {
    '+': Addition,
    '-': Subtraction,
    '*': Multiplication,
    '/': Division
}
