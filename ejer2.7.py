#-------------------------------------------------------------------------------
# Name:        2.7
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
Ejercicio 7.
Definir una lista de números
Encontrar el valor máximo de la lista
Imprimir el valor
No utilizar max
    '''

    lista = [1,3,16,35,15]
    maximo = None
    for i in lista:
        if maximo == None or i > maximo:
            maximo = i

    print(f'El valor maximo es: {maximo}')


if __name__ == '__main__':
    main()
