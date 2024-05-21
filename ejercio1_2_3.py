##Ejercicio 1      ->  Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automatica el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del  cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y si es mayor de 18 deberá pagar 10 soles.

print(    "SALAS DE JUEGO ")
nombre=input("ingrese nombre->")
edad=int(input("ingrese edad ->"))
if edad < 4 :
	print("entra gratis mi estimado")
elif edad < 18 :
	print("el precio a pagar es :  s/ 5.00")
else :		
	print("precio a pagar : s/ 10.00") 


##Ejercicio 2    ->   Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra=input("Introduce una palabra: ")
for i in range(10):
    print(palabra)


## Ejercicio 3   ->   Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


numero= int(input("Introduce un número entero positivo-> "))
for i in range(1, numero+1, 2):
    print(i, end=", ")