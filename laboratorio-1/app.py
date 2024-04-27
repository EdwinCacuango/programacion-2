""" 
    Este programma es una calculadora que permite al usuario elegir entre 
    6 operaciones matemáticas básicas.

    Dependiendo de su elección el programa solicitará los operadores necesarios

    Maneja errores para división de cero y en el caso de que no se ingrese un valor numérico

 """

from make_operations import make_operation

operations ={
    1: "Suma",
    2: "Resta",
    3: "Multiplicación",
    4: "División",
    5: "Potencia",
    6: "Raíz",
    7: "Salir"
}

custom_texts = {
    "Suma": {
        "value_1": "Ingrese el primer sumando: ",
        "value_2": "Ingrese el segundo sumando: ",
        "result": "El resultado de la suma es: ",
    },
    "Resta": {
        "value_1": "Ingrese el minuendo: ",
        "value_2": "Ingrese el sustraendo: ",
        "result": "El resultado de la resta es: ",
    },
    "Multiplicación": {
        "value_1": "Ingrese el primer factor: ",
        "value_2": "Ingrese el segundo factor: ",
        "result": "El resultado de la multiplicación es: ",
    },
    "División": {
        "value_1": "Ingrese el dividendo: ",
        "value_2": "Ingrese el divisor: ",
        "result": "El resultado de la división es: ",
    },
    "Potencia": {
        "value_1": "Ingrese la base: ",
        "value_2": "Ingrese el exponente: ",
        "result": "El resultado de la potencia es: ",
    },
    "Raíz": {
        "value_1": "Ingrese el radicando: ",
        "value_2": "Ingrese el índice: ",
        "result": "El resultado de la raíz es: ",
    }
}

#Desde acá comienza el programa

STATE = True

while STATE:
    print("Bienvenido a la calculadora \n")
    print("Estas son las opciones disponibles:")
    for operation, operation_name in operations.items():
        print(f"{operation}. {operation_name}")

    select_operation = int (input("\nElija el número correspondiente de la operación que desea realizar: "))

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
                    print("\nEl valor ingresado no es un número. Por favor ingrese un valor numérico")
                    value_1 = float(input(f"\n{custom_texts[operation_name]['value_1']}"))
                try:
                    value_2 = float(input(f"\n{custom_texts[operation_name]['value_2']}"))
                    break
                except ValueError:
                    print("\nEl valor ingresado no es un número. Por favor ingrese un valor numérico")
                    value_1 = float(input(f"\n{custom_texts[operation_name]['value_1']}"))
            result = make_operation(operation_name, value_1, value_2)
            print(f"{custom_texts[operation_name]['result']}{result}")
            break
