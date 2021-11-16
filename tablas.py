def tabla(numero):
    print("Esta es la tabla del " + str(numero))
    for i in range(2, 11):
        print(i * numero)    

def run():
    menu = """
    Bienvenido a Tablas de multiplicar
    a. Tabla del 2
    b. Tabla del 3
    c. Tabla del 4
    d. Tabla del 5
    e. Tabla del 6
    f. Tabla del 7
    g. Tabla del 8
    h. Tabla del 9
    i. Tabla del 10

    Elige una opción:
    """
    opcion = str(input(menu))
    if opcion == "a":
        tabla(2)
    elif opcion == "b":
        tabla(3)
    elif opcion == "c":
        tabla(4)
    elif opcion == "d":
        tabla(5)
    elif opcion == "e":
        tabla(6)
    elif opcion == "f":
        tabla(7)
    elif opcion == "g":
        tabla(8)
    elif opcion == "h":
        tabla(9)
    elif opcion == "i":
        tabla(10)
    else:
        print("Ingresa una opción válida")

if __name__ == "__main__":
    run()

    

