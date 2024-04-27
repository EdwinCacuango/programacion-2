def make_operation(operation, value_1, value_2):
    """ Esta funcion recibe la key  de la operacion y comprueba si coincide con alguna de las operaciones

        En función de la operación, usa value_1 y value_2 para operar

        Este devuelve la operación realizada o el error en el caso detectado
    """

    if operation == "Suma":
        return value_1 + value_2
    elif operation == "Resta":
        return value_1 - value_2
    elif operation == "Multiplicación":
        return value_1 * value_2
    elif operation == "División":
        if value_2 == 0:
            raise ZeroDivisionError
        return value_1 / value_2
    elif operation == "Potencia":
        return value_1 ** value_2
    elif operation == "Raíz":
        if value_2 == 0:
            raise ZeroDivisionError
        return value_1 ** (1 / value_2)
    else:
        raise ValueError("Operación no encontrada")

