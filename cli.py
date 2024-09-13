"""" This module has class definition both abstract and concrete
    for calculator
    
    Author: Julian David Celis Giraldo
    This file is parte of PyCalculator - UD
    
    PyCalculator 
    #       Tarea 1
    #   Configurar entorno virtua de python
    #   Activar entorno virtual

    #       Tarea 2
    #   pypi
    #       Tarea 3
    #   PEP (Sugerencias de adición o cambios para Python)
    #       Tarea 4
    #   Poetry -> Libreria que solo permite instalar las dependencias necesarias)
    #   Poetry -> Libreria que no permite generar conflictos entre dependencias
    #   pip freeze -> Librerias instaladas
    #   Black -> Formateador de código
    #   Instalar dependencias
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
            print(f"result:{SimpleCalculator.suma(a,b)}")
        elif option == 2:
            a = float(input("Add first number of the rest:"))
            b = float(input("Add first number of the rest: "))
            print(f"result:{SimpleCalculator.rest(a,b)}")
            
        elif option == 3:
            a = float(input("Add first number of the multiplication:"))
            b = float(input("Add first number of the multiplication: "))
            print(f"result:{SimpleCalculator.multiplication(a,b)}")
        elif option == 4:
            a = float(input("Add first number of the division:"))
            b = float(input("Add first number of the division: "))
            print(f"result:{SimpleCalculator.division(a,b)}")
        elif option == 5:
            a = int(input("Add first number of the power:"))
            b = int(input("Add first number of the power: "))
            print(f"result:{SimpleCalculator.power(a,b)}")

        else: print("Please , choice a valid option")
        option = int(input(MENU))
        
    