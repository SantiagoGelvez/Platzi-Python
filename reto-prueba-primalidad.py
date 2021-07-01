def wilson(numero):
    multiplica = 1
    for i in range(1,numero):
        multiplica = multiplica * i # Calcula el factorial (n-1)
    return multiplica + 1


def primo(numero):
    es_primo = True
    numero_wilson = wilson(numero) % numero # Calcula si (n-1)! + 1 es multiplo de n
    if numero_wilson != 0 or numero == 1: # El 1 no es primo
        es_primo = False
    return es_primo


def run():
    numero = int(input('Escriba un numero: '))
    es_primo = primo(numero)
    if es_primo:
        print('Es un numero primo')
    else:
        print('No es un numero primo')


if __name__ == '__main__':
    run()