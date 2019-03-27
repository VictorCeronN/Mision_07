#Victor Manuel Cerón Navarrete
#Divide restando y calcula el mayor de un conjunto de números

def dividir(dividendo, divisor):

    contador = 0

    residuo = 0

    residuo += dividendo

    while residuo >= divisor:
        valor  = residuo - divisor
        residuo=valor
        contador = contador + 1
    print(dividendo, "/", divisor, "=", contador, ", sobra ", residuo)


def encontrarMayor():   #El programa te dirá constantemente cual es el mayor número hasta que salgas al menú
    print("Teclea una serie de números para encontrar el mayor")
    int(input("Teclea un número [-1 para salir]: "))
    mayor = 0
    a = mayor

    while a != -1:
        a = int(input("Teclea un número [-1 para salir]: "))

        if a >= mayor:
            mayor = a
            print(mayor)

        if a < 0:
            print("ERROR")

        if mayor > 0:
            print("El número mayor es", mayor)

    else:
         print("No existe un valor mayor")


def main():
    print("Misión 07. Ciclios while")
    print("Autor: Victor Manuel Cerón Navarrete")
    print("Matrícula: A01374446")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")

    alfa= int(input("Teclea tu opción: "))



    while alfa != 3:
        if alfa < 1 or alfa >3:

            print("ERROR, el número debe ser del 1 al 3")
            print("Misión 07. Ciclios while")
            print("Autor: Victor Manuel Cerón Navarrete")
            print("Matrícula: A01374446")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")

            alfa = int(input("Teclea tu opción: "))

        if alfa ==1:

            dividendo=int(input("Teclea el dividendo"))
            divisor=int(input("Teclea el divisor"))
            dividir(dividendo, divisor)

            print("Misión 07. Ciclios while")
            print("Autor: Victor Manuel Cerón Navarrete")
            print("Matrícula: A01374446")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")

            alfa = int(input("Teclea tu opción: "))


        elif alfa == 2:
            encontrarMayor()
            print("Misión 07. Ciclios while")
            print("Autor: Victor Manuel Cerón Navarrete")
            print("Matrícula: A01374446")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")

            alfa= int(input("Teclea tu opción: "))
            print("Teclea una serie de números para encontrar el mayor.")
            int(input("Teclea un número[-1 para salir]"))

        else:
            print("FIN")
            quit()




main()