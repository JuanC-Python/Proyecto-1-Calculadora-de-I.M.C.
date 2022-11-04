print("""Bienvenido a la Calculadora de Índice de masa corporal

Por favor diligenciar la siguiente información: \n""")
pregunta = 1
while pregunta == 1:
    nombre = input("Por favor ingrese su nombre: ")
    if not nombre:
        print("No ha ingresado ningún dato")
    else:
        apellido1 = input("Por favor ingrese su primero apellido: ")
    if not apellido1:
        print("No ha ingresado ningún dato")
    else:
        apellido2 = input("Por favor ingrese su segundo apellido: ")
    if not apellido2:
        print("No ha ingresado ningún dato")
    else:
        edad = int(input("Por favor ingrese edad: "))
        # if not type (edad) == int:
        #     print("No es una cifra")
        # else:
    if not edad:
        print("No ha ingresado ningún dato")
    else:
        peso = float(input("Por favor ingrese peso: "))
    if not peso:
        print("No ha ingresado ningún dato")
    else:
        estatura = float(input("Por favor ingrese estatura: "))
    if not estatura:
        print("No ha ingresado ningún dato")
    else:
        IMC = peso/estatura ** 2
        print(
            f"Señor {nombre} {apellido1} {apellido2} a sus {edad} años y con un peso de {peso} y una estatura de {estatura}")
        print(f"Su Índice de Masa Corporal (IMC) es: {IMC:.2f} ")
        pregunta = int(input(
            """Gracias por usar la calculadora de IMC, ¿Quieres volver a realizar la medición? \n1 -Si 2 -No \n"""))
#################################################################################################################################3