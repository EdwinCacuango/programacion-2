""" 
    Este programma es una calculadora que permite al usuario elegir entre 
    6 operaciones matemáticas básicas.

    Dependiendo de su elección el programa solicitará los operadores necesarios

    Maneja errores para división de cero y en el caso de que no se ingrese un valor numérico

    ** Importaciones: options_data contiene diccionarios para el menú de opciones 
    y los textos personalizados para cada operación **

    ** Importaciones: make_operations contiene la función que realiza las operaciones matemáticas 
    y que devuelve el resultado**

 """

from make_operations import make_operation
from options_data import operations, custom_texts

STATE = True

print("Bienvenido a la calculadora \n")

while STATE:
    print("Estas son las opciones disponibles:")
    for operation, operation_name in operations.items():
        print(f"{operation}. {operation_name}")

    select_operation = int(input("\nElija el número correspondiente de la operación que desea realizar."
                                 "Presione 7 para salir: "))

    if select_operation == 7:
        print("Gracias por usar la calculadora")
        STATE = False
        break
    for operation, operation_name in operations.items():
        if select_operation == operation:
            print(f"\nUsted ha seleccionado la operación: {operation_name}")

            while True:
                try:
                    value_1 = float(input(f"\n{custom_texts[operation_name]['value_1']}"))
                except ValueError:
                    print("\nEl valor ingresado no es un número."
                        "Por favor ingrese un valor numérico.")
                    value_1 = float(input(f"\n{custom_texts[operation_name]['value_1']}"))
                while True:
                    try:
                        value_2 = float(input(f"\n{custom_texts[operation_name]['value_2']}"))
                        break
                    except ValueError:
                        print("\nEl valor ingresado no es un número."
                        "Por favor ingrese un valor numérico.")
                break
    
            try:
                result = make_operation(operation_name, value_1, value_2)
            except ZeroDivisionError:
                print("\nNo se puede dividir por cero. Por favor intente nuevamente")
                print("--------------------------- \n")
                continue
            print(f"\n{custom_texts[operation_name]['result']}{result} \n")
            print("--------------------------- \n")
            break
