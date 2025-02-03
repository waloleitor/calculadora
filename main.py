#Calculadora
#Autor: @waloleitor
#Fecha: 03/02/2025
#Descripción: Calculadora básica para novatos
#Licencia: MIT

import funcion_raizcuadrada as frc, funcion_porciento as fpc, funcion_suma as fs, funcion_resta as fr
import funcion_multiplicacion as fm, funcion_division as fd

while True:
    print("Calculadora")
    print("Qué operación deseas realizar?")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz cuadrada")
    print("6. Porcentaje")
    print("7. Salir")
    
    try:
        opcion = int(input("Opción: "))
    
        if opcion > 7 or opcion < 1:
            print("Opción incorrecta")
            continue
        elif opcion == 7:
            break
        elif opcion == 5:
            n = float(input("Número: "))
            print(frc.raiz_cuadrada(n))
        elif opcion == 6:
            n = float(input("Número: "))
            p = float(input("Porcentaje: "))
            print(fpc.porciento(n, p))
        else:
            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))
            if opcion == 1:
                print(fs.sumar(n1, n2))
            elif opcion == 2:
                print(fr.restar(n1, n2))
            elif opcion == 3:
                print(fm.multiplicar(n1, n2))
            elif opcion == 4:
                if n2 == 0:
                    print("No se puede dividir por cero")
                    continue
                else:
                    print(fd.dividir(n1, n2))
    except ValueError:
        print("Debes ingresar un número")
    print()
print("Adiós!")
