from random import randint
from libreria1 import *
import os
os.system("color F4")
os.system("Title ADIVINA EL NUMERO uwu")


def comprobar_numero():
    pass


def adivina_numero():
    num_random = randint(1, 100)

    num_user = input("\nCual es el numero que estoy pensando? ")
    while True:
        try:
            num_user = int(num_user)
            break
        except ValueError:
            num_user = input("Por favor Ingresa un número: ")
            continue

    while num_user <= 0:
        num_user = int(input("Porfavor ingrese un numero mayor a 0: "))

    cantidad_intentos = 1

    while cantidad_intentos <= 5:
        if num_user == num_random:
            print(f"\nLo has adivinado en el intento {cantidad_intentos}")
            numdibujo(cantidad_intentos)
            break
        if num_user > num_random:
            print(f"\nEl número {num_user} es muy alto !!")
            num_user = int(input("Vuelva a intentarlo: "))

        elif num_random > num_user:
            print(f"\nEl número {num_user} es muy bajo !!")
            num_user = int(input("Vuelva a intentarlo: "))
        cantidad_intentos += 1

    if cantidad_intentos == 6:
        print(f"\nLo has adivinado en el intento {cantidad_intentos}")
        numdibujo(cantidad_intentos)

    if num_user != num_random:
        numdibujo(10)
        print(f"El número era {num_random}")

    volver_a_jugar = input("\nDesea volver a jugar? (Y/N) ").upper()
    while volver_a_jugar != "Y" and volver_a_jugar != "N":
        volver_a_jugar = input("\nComando no reconocido (Y/N) ")
        volver_a_jugar = volver_a_jugar.upper()

    match volver_a_jugar:
        case "Y":
            os.system("cls")
            adivina_numero()

        case "N":
            os.system("cls")
            print("\nbtw, gracias por usar el programa.")
            return


# ENTRADA
name_user = input("Hola, cual es su nombre? ")
name_user = name_user.replace(" ", "-").title()


while name_user == "":
    name_user = input("Por favor inserte un nombre: ")
    name_user = name_user.replace(" ", "-").title()
print(f"Bueno, {name_user}, he pensado un número entre 1 y 100, y tienes"
      f" solo 6 intentos para adivinar cuál crees que es el número")
adivina_numero()
