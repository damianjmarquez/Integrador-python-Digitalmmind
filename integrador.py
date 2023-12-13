# Jugar a “piedra, papel, tijera” compitiendo contra la computadora.
# Adivinar un número compitiendo contra la computadora.
# Tirar un dado.
# Graficar una función matemática.
import random
import matplotlib.pyplot as plt
import numpy as np
menu = """
***************************************************************************
*                    1- Piedra, Papel o tijera                            *
*                    2- Adivina el numero                                 *
*                    3- Tirar un dado                                     *
*                    4- grafica una funcion matamatica                     *
***************************************************************************"""
seguir = "SI"
print()
print("**********************BIENVENIDO AL CASINO JOGO BONITO**********************")
print("""A continuacion podra elegir una serie de juegos disponibles y sumar puntos "
      "para disfrutar de esta divertida experiencia, que lo disfrutes""")
print()
nombre = input("ingresa tu nombre ")
print()
print("     HOLA " + nombre + " A CONTINUACION VERAS UN MENU CON LOS JUEGOS DEL CASINO")


piedra = """
             PIEDRA
              oooo
          oo       oo
      oo             oo
    oo                   oo
    ooooooooooooooooooooooo
"""

papel = """
        PAPEL
   |||||||||||||||
   ||           ||
   || ......... ||
   ||           ||
   ||           ||
   || ......... ||
   ||           ||
   ||           ||
   |||||||||||||||

"""

tijera = """
            TIJERA
                           ///
      00              ///
    000000       ///
      00 //////
      00 //////
    000000       ///
      00             ///
                          ///

"""

dados = ["""
            =========
            |       |
            |   *   |
            |       |
            =========

    ""","""
            =========
            | *     |
            |       |
            |     * |
            =========

        ""","""
            =========
            | *     |
            |   *   |
            |     * |
            =========

            ""","""
            =========
            | *   * |
            |       |
            | *   * |
            =========

            ""","""
            =========
            | *   * |
            |   *   |
            | *   * |
            =========

            ""","""
            =========
            | *   * |
            | *   * |
            | *   * |
            =========

            """]





jugar_ppt = "SI"
sumar_valor_jugador = 0
sumar_valor_maquina = 0

while seguir == "SI":
    print(menu)
    print()
    opcion = int(input(" Ingresa el numero del juego con el que te gustaria comenzar: "))
    print()
    if opcion == 1:
        print("************ BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA ************ ")
        print()
        jugar_ppt = "SI"
        while jugar_ppt == "SI":
            valor_aleatorio = random.randint(1, 3)
            jugador = input(nombre + " Te voy a pedir que ingreses piedra papel o tijera ").upper()

            if jugador == "PIEDRA" and valor_aleatorio == 1:
                print(nombre + " has elegido ")
                print(piedra)
                print("Tu contrincante eligió ")
                print(piedra)
                print("HAY UN EMPATE ")
                print("Esto significa que ningun participante suma puntos ")
                jugar_ppt = input("Deseas volver a jugar otra partida? si/no").upper()
            else:
                if jugador == "PIEDRA" and valor_aleatorio == 2:
                    print()
                    print(nombre + " has elegido ")
                    print(piedra)
                    print("Tu contrincante eligió ")
                    print(papel)
                    print("has perdido ")
                    print("Esto significa que tu contrincante se lleva el punto de esta partida ")
                    sumar_valor_maquina = sumar_valor_maquina + 1
                    jugar_ppt = input("Deseas volver a jugar otra partida? si/no").upper()
                if jugador == "PIEDRA" and valor_aleatorio == 3:
                    print()
                    print(nombre + " has elegido ")
                    print(piedra)
                    print("Tu contrincante eligió ")
                    print(tijera)
                    print("has ganado ")
                    print("Esto significa que tu te llevas el punto de esta partida ")
                    sumar_valor_jugador = sumar_valor_jugador + 1
                    jugar_ppt = input("Deseas volver a jugar otra partida? si/no").upper()

            if jugador == "PAPEL" and valor_aleatorio == 1:
                print(nombre + " has elegido ")
                print(papel)
                print("Tu contrincante eligió ")
                print(piedra)
                print("HAS GANADO")
                print("Esto significa que tu  sumas un punto ")
                sumar_valor_jugador = sumar_valor_jugador + 1
                jugar_ppt = input("Deseas volver a jugar otra partida? si/no").upper()
            else:
                if jugador == "PAPEL" and valor_aleatorio == 2:
                    print()
                    print(nombre + " has elegido ")
                    print(papel)
                    print("Tu contrincante eligió ")
                    print(papel)
                    print("HAY UN EMPATE ")
                    print("Esto significa que ningun jugador se lleva el punto ")
                    jugar_ppt = input("Deseas volver a jugar otra partida? si/no").upper()
                if jugador == "PAPEL" and valor_aleatorio == 3:
                    print()
                    print(nombre + " has elegido ")
                    print(papel)
                    print("Tu contrincante eligió ")
                    print(tijera)
                    print("has perdido ")
                    print("Esto significa que tu contrincante se lleva el punto de esta partida ")
                    sumar_valor_maquina = sumar_valor_maquina + 1
                    jugar_ppt = input("Deseas volver a jugar otra partida? si/no").upper()

            if jugador == "TIJERA" and valor_aleatorio == 1:
                print(nombre + " has elegido ")
                print(tijera)
                print("Tu contrincante eligió ")
                print(piedra)
                print("HAS PERDIDO")
                print("Esto significa que tu contrincante suma un punto ")
                sumar_valor_maquina = sumar_valor_maquina + 1
                jugar_ppt = input("Deseas volver a jugar otra partida? si/no").upper()

            elif jugador == "TIJERA" and valor_aleatorio == 2:
                    print()
                    print(nombre + " has elegido ")
                    print(tijera)
                    print("Tu contrincante eligió ")
                    print(papel)
                    print("HAS GANADO")
                    print("Esto significa que tu te llevas el punto ")
                    sumar_valor_jugador = sumar_valor_jugador + 1
                    jugar_ppt = input("Deseas volver a jugar otra partida? si/no").upper()
            elif jugador == "TIJERA" and valor_aleatorio == 3:
                    print()
                    print(nombre + " has elegido ")
                    print(tijera)
                    print("Tu contrincante eligió ")
                    print(tijera)
                    print("HAN EMPATADO ")
                    print("Esto significa que ningun jugador se lleva el punto ")
                    jugar_ppt = input("Deseas volver a jugar otra partida? si/no").upper()
            else:
                print()
                print("La opcion que elegiste no es la correcta")
                print()

        if sumar_valor_jugador > sumar_valor_maquina:
            print("EL RESULTADO FINAL ES: ")
            print("*******************************")
            print("*                             *")
            print("* ", nombre, "    ", sumar_valor_jugador, "             *")
            print("* " + "Computador: ", sumar_valor_maquina, "             *")
            print("*  FELICITACIONES HAS GANADO  *")
            print("*                             *")
            print("*******************************")
        if sumar_valor_jugador < sumar_valor_maquina:
            print("EL RESULTADO FINAL ES: ")
            print("*******************************")
            print("*                             *")
            print("* " + nombre, sumar_valor_jugador, "                   *")
            print("* " + "Computador: ", sumar_valor_maquina, "             *")
            print("*    OHHH NOOOO PERDISTE      *")
            print("*                             *")
            print("*******************************")
        if sumar_valor_jugador == sumar_valor_maquina:
            print("EL RESULTADO FINAL ES: ")
            print("*******************************")
            print("*                             *")
            print("* " + nombre, sumar_valor_jugador, "                   *")
            print("* " + "Computador: ", sumar_valor_maquina, "             *")
            print("*     ESTO ES UN EMPATE       *")
            print("*                             *")
            print("*******************************")
    elif opcion == 2:
        print("BIENVENIDO A ADIVINA EL NUMERO SOLO TENDRAS 5 INTENTOS PERO TE AYUDAREMOS  VAMOS...")


        def adivinar(numero):
            puntos = 0
            intentos = 5
            otro_intento = "SI"
            while intentos > 0 and otro_intento == "SI":
                print()
                eleccion_numero = int(input(nombre + "Ingresa un numero entre el 1 y el 20: "))
                if intentos == 1:
                    print("se han acabado los intentos")
                    intentos = 5
                    otro_intento = input(" no te quedan intentos desea seguir si/no").upper()
                elif numero < eleccion_numero:
                    print(" TU NUMERO ES MAYOR DEBES ELEGIR UNO MENOR ")
                    intentos = intentos - 1
                elif numero > eleccion_numero:
                    print(" TU NUMERO ES MENOR DEBES ELEGIR UNO MAYOR ")
                    intentos = intentos - 1
                else:
                    print(" HAS GANADO FELICITACIONES EL NUMERO CORRECTO ES  ", numero)
                    puntos = puntos + 1
                    print("tienes: ", puntos, " puntos")
                    intentos = 5
                    numero = random.randint(1, 20)
                    otro_intento = input("desea seguir si/no").upper()

            print("TU RESULTADO FINAL ES: ")
            print("*******************************")
            print("*                             *")
            print("* " + nombre, puntos,  " Puntos            *")
            print("*HICISTE UN EXCELENTE TRABAJO *")
            print("*                             *")
            print("*******************************")


        numero_aleatorio = random.randint(1, 20)
        adivinar(numero_aleatorio)
    elif opcion == 3:
        print("BIENVENIDO A TIRA EL DADO Y SACA 7 ACUMULA PUNTOS ")

        def dado(numero_dado1,numero_dado2):
            intento_dado = input("TIRA LOS DADOS INGRESA Mezclar/SALIR: ").upper()
            while intento_dado == "MEZCLAR":

                resultado = numero_dado2 + numero_dado1

                if resultado == 7:
                    print( "GANASTE")
                    print("------EL PRIMER DADO FUE-------- ")
                    print(dados[numero_dado1 - 1])
                    print("------EL SEGUNDO DADO FUE-------- ")
                    print(dados[numero_dado2 - 1])
                    print("LA SUMA DE TUS DADOS FUE ", resultado)
                    intento_dado = input("TIRA LOS DADOS INGRESA Mezclar/SALIR: ").upper()
                    print("LA SUMA DE TUS DADOS FUE ", resultado)

                else:

                    print( "PERDISTE")
                    print("------EL PRIMER DADO FUE-------- ")
                    print(dados[numero_dado1-1])
                    print("------EL SEGUNDO DADO FUE-------- ")
                    print(dados[numero_dado2 - 1])
                    print("LA SUMA DE TUS DADOS FUE ",resultado)
                    intento_dado = input("TIRA LOS DADOS INGRESA Mezclar/SALIR: ").upper()
                    numero_dado1 = random.randint(1, 6)
                    numero_dado2 = random.randint(1, 6)


            print("GRACIAS POR PARTICIPAR")


        numero_dado1 = random.randint(1, 6)
        numero_dado2 = random.randint(1, 6)
        dado(numero_dado1,numero_dado2)
    elif opcion ==4:
        graficar = "SI"
        while graficar =="SI":
            print("soy la opcion 4")

            # Pedir al usuario que ingrese la fórmula de la función
            formula = input("Ingrese la fórmula de la función (utilice 'x' como variable): ")


            # Convertir la cadena ingresada a una función de Python
            def funcion(x):
                return eval(formula)


            # Pedir al usuario que ingrese los valores del rango
            valor1 = int(input("Ingrese el primer valor del rango: "))
            valor2 = int(input("Ingrese el segundo valor del rango: "))

            # Generar valores de x
            x = np.linspace(valor1, valor2, 100)

            # Calcular los valores de y (f(x))
            y = funcion(x)

            # Graficar la función
            plt.figure(figsize=(8, 6))
            plt.plot(x, y, label=f'{formula}')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Gráfica de la función ingresada por el usuario')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.grid(color='gray', linestyle='--', linewidth=0.5)
            plt.legend()
            plt.show()
            graficar = input(nombre + " Deseas graficar otra función? si/no ").upper()
    else:
        print("La opcion que seleccionaste no esta disponible ")
    seguir = input("Desea elegir otro juego? si/no").upper()




print("GRACIAS " + nombre + "POR ELEGIR JUGAR CON NOSOTROS VUELVE PRONTO TE ESTAREMOS ESPERANDO")

