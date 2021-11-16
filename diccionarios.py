def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])

    paises = {
        "Argentina": 44938712,
        "Brazil": 210_147_125,
        "Colombia": 50372424
    }
    # print(paises["Argentina"])

#     for pais in paises.keys():
#         print(pais)
#Devolverá los valores del diccionario
#     for pais in paises.values():
#         print(pais)

#Devolverá tanto keys como values
    for pais, poblacion in paises.items():
          print(pais + " Tiene " + str(poblacion) + " habitantes")

if __name__ == "__main__":
    run()