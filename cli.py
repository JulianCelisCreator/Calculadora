"""" This module has class definition both abstract and concrete
    for calculator
    
    Author: Julian David Celis Giraldo
    This file is parte of PyCalculator - UD
    
    PyCalculator 
    
"""
from calculator_class import SimpleCalculator   

if __name__ == "__main__":
    MENU = """
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Potencia
    6. Salir"""
    
    option = int(input(MENU))
    while option != 6:
        if option == 1:
            
            a = float(input("Add first number of the sum:"))
            b = float(input("Add first number of the sum: "))
            print(f"result:{SimpleCalculator.sum(a,b)}")
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass

        else: print("Please , choice a valid option")
        option = int(input(MENU))
        
    