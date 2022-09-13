#-------------------------------------------------------------------------------
# Name:        2.4
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
Ejercicio 4.
Definir una lista
Contar los elementos de esa lista
Al finalizar mostrar por pantalla la cantidad de elementos de la lista
No utilizar función len
    '''

    contar = 0
    lista = [1,3,16,35,15]
    for i in lista:
        contar = contar + 1

    print(f'La cantidad de elementos son: {contar}')
    print("fin")

if __name__ == '__main__':
    main()
