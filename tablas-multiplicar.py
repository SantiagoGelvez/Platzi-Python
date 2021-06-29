def run():
    titulo = """
    Programa para mostrar la tabla de multiplicar que quieras

    """
    print(titulo)
    prog = True
    while prog:
        tabla = int(input("Dime cual tabla quieres (numero entero): "))
        for multiplicando in range(11):
            print(str(tabla) + " X " + str(multiplicando) + " = " + str(tabla * multiplicando))
        continua = input("Quieres consultar otra tabla? (1-Si, 0-No): ")
        if continua == '1':
            pass
        else:
            prog = False


if __name__ == '__main__':
    run()