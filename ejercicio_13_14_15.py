#ejercicio 13
while True:
    print("\tCALCULADORA")
    a=int(input("ingrese dato a ->"))
    b=int(input("ingrewse dato b ->"))
    print("""1. calcular la suma de A y B 
 2. calcular A/B. vigilamos que B no sea 0..
 3.carcular (A*B) /2.5
 4. salir.""")
    opcion=int(input("ingrese opcion->"))
    if opcion ==1:
        raiz_cuadrada=(a+b)**0.5
        print(f"la raiz cuadrada del resultadiom nes {raiz_cuadrada}\n")
    if  opcion == 2:
        division= a/b  
        print(f"la divivion es {division}\n")
    if b == 0 :
        print ("divicion entre cero no aseptable")
    if opcion == 3 : 
        resultado=(a*b)/2.5
        print(f"el resultado es {resultado}\n") 
    elif opcion == 4 :
        print("\ngracias por su visita")
        break


                                   






## ejercicio 14
contraseña="hola mundo"
contador=3
while contador > 0:
    contra=input("ingrese contraseña -> ")
    if contra == contraseña:
        print(f"login correct")
        break
    else:
        contador-=1
        print(f"te quedan {contador} intentos")
        if contador == 0 :
            print("llamando policia ,  choro a la vista")

## ejercicio 15:
numero_1,numero_2=0,1
while numero_2<90:
    print(numero_1,numero_2,end="")
    numero_1+=numero_2
    numero_2+=numero_1


        
