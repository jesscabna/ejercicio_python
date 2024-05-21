##Ejercicio 10    -> Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

##Ejercicio 11  Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números (que puedan ser decimales) y calcule su suma, mostrar por terminal la suma de los números introducidos.


print ("¿Cuántos numeros va a introducir ?")
num = int(input())

suma=0
for numero in range(1,num+1):
    print(" Escribe el numero %s"% str(numero))
    num_=float(input())
    suma= suma+num_
print ("La suma de los %s numeros introducidos es %s"% (str(num),str(suma)))


##Ejercicio 12    -> Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
print ("Cuantos numeros desea introducir?")
num=int(input())

contador=0
for numero in range(1,num+1):
    print ("Escriba el numero %s"% str(numero))
    nNumeros=float(input())
    if nNumeros<0:
        contador=contador+1
        
print ("Ha introducido %s numeros negativos."% str(contador))

