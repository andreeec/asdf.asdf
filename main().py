import libreria_complejos

def main():

    print("este programa puede realiar operaciones basicas con numeros complejos")
    print("para usarlo debe indicar el numero de la operacion que desea realizar")
    print("Suma = 1")
    print("Producto = 2")
    print("Resta = 3")
    print("División = 4")
    print("Módulo = 5")
    print("Conjugado = 6") 
    print("luego debe introducir el numero comlejo primero la parte real y luego l aimaginaria")

    num = int(input("ingrese el numero de la operacion que desea realizar"))

    numero1 = []
    numero2 = []

    if num == 1:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)

        for j in range(2):
            b = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero2.append(b)

        c = libreria_complejos.suma_complejos(numero1, numero2)
    elif num == 2:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)

        for j in range(2):
            b = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero2.append(b)
        
        c = libreria_complejos.multiplicacion_complejos(numero1, numero2)
    elif num == 3:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)

        for j in range(2):
            b = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero2.append(b)
        
        c = libreria_complejos.resta_complejos(numero1, numero2)
    elif num == 4:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)

        for j in range(2):
            b = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero2.append(b)

        c = libreria_complejos.divicion_complejos(numero1, numero2)
    elif num == 5:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)
        c = modulo_complejos(numero1)
    elif num == 6:
        for i in range(2):
            n = int(input("ingrese los valores del numero primero l aparte real y luego la imaginaria"))
            numero1.append(n)
        c = libreria_complejos.conjugado_complejos(numero1)
    else:
        print("el numero d eoperacion que desa realizar no existe")
        
    #print(numero1)
    #print(numero2)
    
    print (c)
    

