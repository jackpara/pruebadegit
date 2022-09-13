#-------------------------------------------------------------------------------
# Name:        2.6
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
Ejercicio 6.
Definir una lista de números
Mostrar por pantalla el valor promedio de la lista.
No utilizar funciones sum ni len
    '''

    lista = [1,3,16,35,15]
    suma = 0
    contar = 0
    for item in lista:
        suma = suma + item
        contar = contar + 1

    prom = suma / contar
    print(f'el promedio es: {prom}')

if __name__ == '__main__':
    main()
