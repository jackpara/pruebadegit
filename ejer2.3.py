#-------------------------------------------------------------------------------
# Name:        2.3
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
Ejercicio 3.
Pedir al usuario que ingrese un email
Verificar si el usuario ingresó una dirección de email (basta con que tenga un
"@")
Al finalizar mostrar por pantalla si es un email o no
No utilizar in
    '''

    email = input("Ingrese un email: ")

    for arroba in email:
        if(arroba == "@"):
            arroba = True
            break
        if arroba == False:
            break

    if arroba == True:
        print(f'({email}) ,Si es un email')
    else:
        print(f'({email}) ,No es un email')
    print("fin")

if __name__ == '__main__':
    main()
