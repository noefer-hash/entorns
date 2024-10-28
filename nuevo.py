import math

def ejercicio_1():
    A = input("Introduce el valor de A: ")
    B = input("Introduce el valor de B: ")
    print(f"Valores iniciales - A: {A}, B: {B}")
    A, B = B, A



def ejercicio_2():
    num1 = float(input())
    num2 = float(input())
    suma= num1+num2
    resta=  num1-num2
    multiplicacion=  num1*num2
    if  num2 != 0:
        division=   num1/num2
    else:
     division=  "No se puede dividir entre cero"
    print(f"La suma es: {suma}")
    print(f"La resta es: {resta}")
    print(f"La multiplicación es: {multiplicacion}")
    print(f"La división es: {division}")



def ejercicio_3():
 num1 = float(input("Introduce el primer número: "))
 num2 = float(input("Introduce el segundo número: "))

 if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
 elif num1 < num2:
    print(f"El número {num2} es mayor que {num1}")
 else:
    print(f"El número {num1} es igual que {num2}")



def ejercicio_4():
 num1 = float(input("ingrese el primer numero:"))
 num2 = float(input("ingrese el segundo numero:"))
 num3=  float(input("ingrese el tercer numero:"))
 if num1 > num2 and num1 > num3:
    print(f"El número {num1} es el mayor")
 elif num2 > num1 and num2 > num3:
    print(f"El número {num2} es el mayor")
 else:
    print(f"El número {num3} es el mayor")



def ejercicio_5():
# Solicitar tres números al usuario
 num1 = float(input("ingrese el primer numero"))
 num2 = float(input("ingrese el segundo numero"))
 num3 = float(input("ingrese el tercer numero"))

# Decidir si realizar producto o suma
 if num1 < 0:
    producto = num1*num2*num3
    print(f"El producto de los tres números es: {producto}")
 else:
    suma = num1 + num2 + num3
    print(f"La suma de los tres números es: {suma}")



def ejercicio_6():
 import math
 num =  float(input("ingrese un numero:"))
 if num <= 0:
    print("El número no es positivo")
 else:
    potencia = num **2
    raiz = math.sqrt(num)
    print(f"La raiz cuadrada del número es: {raiz}")
   


if __name__ == "__main__":
    while True:
        print("\nMenú de Ejercicios:")
        print("1. Ejercicio 1 (Intercambiar valores)")
        print("2. Ejercicio 2 (Operaciones básicas)")
        print("3. Ejercicio 3 (Comparar dos números)")
        print("4. Ejercicio 4 (Encontrar el mayor de tres números)")
        print("5. Ejercicio 5 (Suma o producto de tres números)")
        print("6. Ejercicio 6 (Raíz cuadrada y cuadrado de un número)")
        print("0. Salir")

        opcion = input("Seleccione el número del ejercicio que desea ejecutar: ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

