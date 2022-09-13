#-------------------------------------------------------------------------------
# Name:        2.5
# Purpose:
#
# Author:      User
#
# Created:     11/09/2022
# Copyright:   (c) User 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    '''
Ejercicio 5.
Definir una lista de números
Sumar todos sus valores de esa lista
Al finalizar mostrar por pantalla el total de la suma.
No utilizar función sum
    '''

    lista = [1,3,16,35,15]
    suma = 0
    for item in lista:
        suma = suma + item

    print(f'Total: {suma}')


if __name__ == '__main__':
    main()
