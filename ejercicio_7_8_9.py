##Ejercicio 7  Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))


##Ejercicio 8     Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra = input("Introduce una palabra: ")
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])


##Ejercicio 9     Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.
#*Ejercicio Nueve*
# Escriba un programa que pregunte cuántos números se van a introducir
numeros_a_introducir:str=float(input("¿Cuántos números se va a introducir?: "))
# luego pida esos números
numero_anterior:str=int(input("escriba sus numeros: "))
#y muestre un mensaje cada vez que un número no sea mayor que el anterior.


for n in range(0):
	if numeros_a_introducir < 0:
		print("imposible")
#MAYORES QUE EL ANTERIOR
for i in range(numero_anterior - 1):
	escriba_num:str=input("escriba un numero: ")
if escriba_num >= 10:
	print(f"{escriba_num} no es mayor que 1")
if numero_anterior == escriba_num:
	print("gracias por su colaboracion")
