#-------------------------------------------------------------------------------
# Name:        2.2
# Purpose:
#
# Author:      User
#
# Created:     12/09/2022
# Copyright:   (c) User 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    '''
Ejercicio 2.
Pedir al usuario que ingrese dos nros
Luego imprimir 3 opciones (1. sumar, 2. restar y 3. multiplicar)
Pedir al usuario que ingrese una opción
Verificar la opción del usuario
Mientras que el usuario no ingrese una opción correcta se volverá a pedir que
ingrese una opción
Ejecutar la operación
Mostrar por pantalla el resultado
    '''

    print("Ingresa dos nros: ")
    num1 = int(input("el primero: "))
    num2 = int(input("el segundo: "))
    s = num1+num2
    r = num1-num2
    m = num1*num2

    while True:
        print("Tienes 3 opciones: 1.sumar, 2.restar, 3.multi.")
        opcion = int(input("Ingresa uno de los 3 numeros: "))

        if opcion == 1:
            print(f'La suma da: {s}')
            break
        elif opcion == 2:
            print(f'La resta da: {r}')
            break
        elif opcion == 3:
            print(f'la multi. da: {m}')
            break
        else:
            print("error")
    print("fin")

if __name__ == '__main__':
    main()
