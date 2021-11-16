def run():
    print("Te reto a adivinar mi número en mente. \n Tienes solo 3 intentos")
    intentos = 0
    respuesta = 10

    while intentos < 3:
        adivina = int(input("Cúal es el número?: "))
        intentos = intentos + 1
        if adivina == respuesta:
            print("Has ganado!!!!!!")
            break
        if intentos == 3:
            print("Game over")



if __name__ == "__main__":
    run()
