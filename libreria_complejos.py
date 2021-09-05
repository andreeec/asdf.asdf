def suma_complejos(numero1, numero2):
    """ funcion para sumar numeros complejos """

    a = numero1[0] + numero2[0]
    b = numero1[1] + numero2[1]

    c = [a, b]
    
    return c

def multiplicacion_complejos(numero1, numero2):
    """ funcion para multiplicar numeros complejos """

    a = (numero1[0] * numero2[0]) - (numero1[1] * numero2[1])
    b = (numero1[0] * numero2[1]) - (numero1[1] * numero2[0])

    c = [a, b]
    
    return c

def divicion_complejos(numero1, numero2):
    """ funcion para dividir  numeros complejos """

    a = ((numero1[0] * numero2[0]) - (numero1[1] * numero1[1]))/numero2[0]**2 - (numero2[1]**2*-1)
    b = ((numero1[0] * numero2[1]) + (numero1[1] * numero2[1]))/numero2[0]**2 - (numero2[1]**2*-1)

    c = [a, b]
    
    return c

def resta_complejos(numero1, numero2):
    """ funcion para sumar numeros complejos """

    a = numero1[0] - numero2[0]
    b = numero1[1] - numero2[1]

    c = [a, b]
    
    return c

def modulo_complejos(numero1):
    """ funcion para obtener el modulo de ub numero complejo """

    a = (numero1[0]**2 + numero1[1]**2)**(1/2)

    c = a
    
    return c

def conjugado_complejos(numero1):
    """ funcion para sumar numeros complejos """

    a = numero1[0]
    b = numero1[1]

    c = [a, -b]
    
    return c

def adc_vcplx (numero1, numero2):
    """ adicion de vectores complejos """

    a = numero1[0] + numero2[0]
    b = numero1[1] + numero2[1]

    c = [a, b]

    return c

def inverso_vcplx (numero1):
    """ entrega el inverso aditivo de un vector complpejo """

    a = numero1[0]
    b = numero1[1]

    c = [-a, -b]
    
    return c

def mul_escalarvcplx (escalar, vector):
    
    z = []
    j = 0
    
    while j < len(vector): #[2, 2, 2, 2, 2]
        a = multiplicacion_complejos(escalar, vector[j])

        z = z + a
        j = j+1

        return z

def adicion_de_matrizecplx (matriz1, matriz2):

    a = []

    for i in range(len(matriz1)):

        b = suma_complejos(matriz1[i], matriz2[i])

        a = a + [b]

    return a


####################################################
def inverso_matrizcplx (matriz1): #(([2,-2],[5,-4],[2,-2],[1,1]))

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):

            matriz1[i][j] = int(matriz1[i][j])
            matriz1[i][j] = -matriz1[i][j]

    return matriz1

####################################################

def traspuesta_matrizcplx(matriz1):

    aux = []
    
    for i in range(len(matriz1)-1):
        for j in range(len(matriz1[0])-1):
                          

            matriz1[i][j] = aux

            matriz1[i][j] = matriz1[j][1]          
                          
            matriz1[j][i] = aux

    return matriz1

def producto_internovvc(vector1, vector2):

    a = 0

    for i in range(len(vector1)):

        b = vector1[i] * vector2[i]
        a = a + b

    return a


def norma_vc(vector1):

    a = 0
    

    for i in range(len(vector1)):
        b = vector1[i]*vector1[i]
        a = a + b
        print (a)

    c = a**0.5

    return c

def distancia_vec(vector1, vector2):

    a = 0
    
    for i in range(len(vector1)):
        
        b = ((vector2[i]-vector1[i])*(vector2[i]-vector1[i]))
        a = a + b
        print (a)

    c = a**0.5

    return c

def producto_tensor(vector1, vector2):
    ba = len(vector1)
    bb = len(vector2)
    bc = ba * bb

    r = [(0,0)] * bc
    aux = 0

    for j in range(ba):
        for f in range(b):
            r[aux] =  multiplicacion_complejos(vector1[j], vector2[f])
            aux = aux + 1

    return r




    
    

