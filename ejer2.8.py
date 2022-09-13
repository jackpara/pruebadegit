#-------------------------------------------------------------------------------
# Name:        2.8
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
Ejercicio 8.
Definir una lista de números
Encontrar el valor mínimo de la lista
Imprimir el valor
No utilizar min
    '''

    lista = [1,3,16,35,15]
    minimo = None
    for i in lista:
        if minimo == None or i < minimo:
            minimo = i

    print(f'El valor minimo es: {minimo}')

if __name__ == '__main__':
    main()
