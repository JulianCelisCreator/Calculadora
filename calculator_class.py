"""
This module has class definition both abstract and concrete
for calculators.

Author: Julian David Celis Giraldo <jdcelisg@udistrital.edu.co>

This file is part of PyCalculator-UD.

PyCalculator-UD is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

PyCalculator-UD is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with PyCalculator-UD. If not, see <https://www.gnu.org/licenses/>. 
"""

# Google Doc Python: Documentación python para cada método
# Doc String
from abc import ABC, abstractmethod
from datetime import datetime
import numpy as np


class AbstractCalculator(ABC):
    """ "
    This class represents the behavior of an abstract calculator.
    """

    def sum(self, a: float, b: float) -> float:
        """This methos sums two numerical values. #Resumen
        This methot takes two arguments, expected as numbers,
        and calculate and return the sum of those ones.

        Args:
            a(float): First number of the sum.
            b(float): Second number of the sum

        Returns:
            A float value with the result of the sum
        """
        return a + b

    def rest(self, a: float, b: float) -> float:
        """This method applies substraction between two numbers

        This method takes two numbers received as arguments and
        calculate the substraction in the given order.

        Args:
            a(float): first numert of the rest
            b(float): Second number of the rest

        returns:
            A float with the result of the substraction

        """
        return a - b

    def multiplication(self, a: float, b: float) -> float:
        """This method applies multiplication between two numbers

        THis method takes two numbers received as arguments
        and calculate the substraction in the given order

        Args:
            a(float): first number of the multiplication
            b(float): Second number of the multiplication

        returns:
            A float with the result of the multiplication

        """
        return a * b

    def division(self, a: float, b: float) -> float:
        """This method calculates the division between two numbers

        THis method takes two numbers received as arguments and calculate the division using
        the native arithmetic operation, but without valition of zero-division

        Args:
            a(float): numerator of the division
            b(float): divisor number of the division

        returns:
            A float with the result of the division

        """
        return a / b

    # metodo abstract tiene la obligación de aparecer en las clases hijas
    @abstractmethod
    # Método abstracto
    def power(self, base: int, exponent: int) -> int:
        """This is an abstract method for calculater power

        Args:
            base(int): base of the power
            b(float): exponent of the power

        returns:
            A int with the result of the power

        """

        return base**exponent


# ================== Concrete Version of a calculator ============================ #


class SimpleCalculator(AbstractCalculator):
    """This class represents the behavior of a simple concrete calculator
    where the methods from abstract class are ihnerated, some improvement
    and new functionalities ared added.
    """

    def __init__(self):
        self.memory = 0

    def division(self, a: float, b: float) -> float:
        """This method calculates the division between two numbers

        This method takes two numbers received as arguments and calculate the division using
        the native arithmetic operation, but including valitaion of zero-division

        Args:
            a(float): numerator of the division
            b(float): divisor number of the division

        returns:
            A float with the result of the division

        """
        try:
            result = a / b
        except Exception as e:
            print(f"ERROR.{e}")
            # Abre log y agrega los errores al log, encoding son los simbolos del teclado
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()} --- ERROR. {e}. ")
            result = np.nan  # Not a number
        return result

    def power(self, base: int, exponent: int) -> int:
        """This is an abstract method for power calculation

        In this method the power is calculated using a loop
        to apply multiplication in a iterative way
        Args:
            base(int): base of the power
            b(float): exponent of the power

        returns:
            A integer with the result of the power

        """
        if exponent == 0:
            result = 1
        else:
            temp = 1
            for _i in range(exponent + 1):
                temp *= base
            result = temp
        return result
