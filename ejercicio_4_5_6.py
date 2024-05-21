##Ejercicio (4)  Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

##Ejercicio 5 -> Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra= input("Introduce una palabra: ")
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])

##- **Ejercicio 6 -> Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de la imagen adjunta.
numero= int(input("introduce un numero entero "))
for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")