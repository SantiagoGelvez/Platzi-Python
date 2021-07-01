def run():
    enunciado = '''
    Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
    Informar cuál fue el mayor número ingresado.
    '''
    print(enunciado)
    mayor = 0
    while True:
        numero = int(input('Ingrese un numero: '))
        if numero == 0:
            print('Fin del programa')
            print('El numero mayor ingresado fue ' + str(mayor))
            break
        elif numero < 0:
            print('Numero incorrecto. Debe ser positivo')
            continue
        else:
            if numero > mayor:
                mayor = numero
            continue


if __name__ == '__main__':
    run()