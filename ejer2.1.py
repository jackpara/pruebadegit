#-------------------------------------------------------------------------------
# Name:        2.1
# Purpose:
#
# Author:      User
#
# Created:     05/09/2022
# Copyright:   (c) User 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    '''
Ejercicio 1.
Pedir al usuario que ingrese un nro impar
Mientras que el usuario no ingrese un nro impar
se volverá a pedir que ingrese un nro impar
Deberá indicar por pantalla si es impar
    '''

    contador = 1
    while True:
        num = int(input("Ingrese un nro impar: "))
        impar = num % 2 == 0
        contador = contador + 1
        if impar == 0:
            print(f'Si es impar el: {num}')
            break
        if impar == 1 and contador > 20:
            break
    print("fin")

if __name__ == '__main__':
    main()
