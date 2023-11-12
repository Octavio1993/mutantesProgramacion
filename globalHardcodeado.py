#creo clase mutante
class mutante:
    #recibe la matriz
    def __init__(self,dnaMatriz):
        self.dnaMatriz = dnaMatriz

    #agrego el metodo isMutant pedido por el ejercicio
    def isMutant(self):
        #guardo el len de la matriz
        n = len(self.dnaMatriz)

        #contador de secuencias iguales
        contador = 0

        #recorro matriz para buscar las letras iguales
        for i in range(n):
            for j in range(n - 3):
                #verifico las horizontales
                secHorizontal = self.dnaMatriz[i][j:j + 4]
                if self.secuencia(secHorizontal):
                    contador += 1
                    if contador > 1:
                        return True
        
        for i in range(n - 3):
            for j in range(n):
                #verifico las verticales
                if self.secuencia([self.dnaMatriz[k][j] for k in range(i, i + 4)]):
                    contador += 1
        

        for i in range(n - 3):
            for j in range(n - 3):
                
                #verifico diagonal izquierda-derecha
                secDiagonalIzqDer = [self.dnaMatriz[i + k][j + k] for k in range(4)]
                if self.secuencia(secDiagonalIzqDer):
                    contador += 1
                
                #verifico diagonal derecha-izquierda
                secDiagonalDerIzq = [self.dnaMatriz[i + k][j + 3 - k] for k in range(4)]
                if self.secuencia(secDiagonalDerIzq):
                    contador += 1
                
        if contador > 1:
            return True

    #verifico si hay 4 letras iguales seguidas        
    def secuencia(self,secuencia):
        return len(set(secuencia)) == 1


def opcionesCreadas(elegirMatriz):
    matrices = {
        #matriz no mutante
        1: [
            ["A", "T", "G", "C", "G", "A"],
            ["C", "A", "G", "T", "G", "C"],
            ["T", "T", "A", "T", "T", "T"],
            ["A", "G", "A", "C", "G", "G"],
            ["G", "C", "G", "T", "C", "A"],
            ["T", "C", "A", "C", "T", "G"]
        ],
        #matriz mutante horizontal
        2: [
            ["A", "T", "G", "C", "G", "A"],
            ["C", "C", "C", "C", "G", "C"],
            ["T", "A", "T", "T", "T", "T"],
            ["A", "G", "A", "A", "G", "G"],
            ["C", "C", "C", "C", "T", "A"],
            ["T", "C", "A", "C", "T", "G"]
        ],
        #matriz mutante vertical
        3: [
            ["A", "T", "G", "C", "G", "A"],
            ["A", "A", "G", "T", "G", "C"],
            ["A", "T", "A", "T", "T", "T"],
            ["A", "G", "A", "T", "G", "G"],
            ["C", "C", "C", "T", "T", "A"],
            ["T", "C", "A", "C", "T", "G"]
        ],
        #matriz mutante diagonal
        4: [
            ["A", "T", "G", "C", "G", "A"],
            ["C", "A", "G", "T", "G", "C"],
            ["T", "T", "A", "G", "T", "T"],
            ["A", "G", "G", "A", "G", "G"],
            ["A", "G", "C", "C", "T", "A"],
            ["T", "C", "A", "C", "T", "G"]
        ],
        #matriz mutante combinada
        5: [
            ["A", "T", "G", "C", "G", "A"],
            ["C", "A", "G", "T", "G", "C"],
            ["T", "T", "A", "T", "T", "T"],
            ["A", "G", "A", "A", "T", "G"],
            ["C", "C", "C", "C", "T", "A"],
            ["T", "C", "A", "C", "T", "G"]
        ]
    }

    return matrices.get(elegirMatriz)

def opcionesMatrices():
    print("Opciones de matrices para ejecutar el programa")
    print("1. Matriz 1")
    print("2. Matriz 2")
    print("3. Matriz 3")
    print("4. Matriz 4")
    print("5. Matriz 5")

def mostrarMatriz(dnaMatriz):
    print("Matriz elegida por el usuario")
    for row in dnaMatriz:
        print(" ".join(row))

def validacionRespuesta(respuesta):
    resp = respuesta.lower()
    while resp != "s" and resp != "n":
        print("La respuesta debe ser solamente S o N")
        respuesta = input("Ingrese nuevamente su respuesta")
    if resp == "s":
        return True
    elif resp == "n":
        return False


continuar = True
while continuar:
    #doy a elegir al usuario una lista de matrices ya cargadas
    opcionesMatrices()

    #le pregunto que opcion desea elegir
    elegirMatriz = int(input("Ingrese el número de la matriz a usar: "))

    #traigo la matriz que eligió el usuario
    dnaMatriz = opcionesCreadas(elegirMatriz)
    
    if dnaMatriz:
        #muestro la matriz ingresada
        mostrarMatriz(dnaMatriz)

        #instancio un objeto tipo mutante, le paso la matriz
        detector = mutante(dnaMatriz)

        #me fijo si la matriz ingresada corresponde a un mutante
        esMutante = detector.isMutant()

        #muestro si el adn ingresado corresponde o no a un mutante
        if esMutante:
            print("El ADN ingresado corresponde a un mutante")
        else:
            print("El ADN ingresado NO corresponde a un mutante")
    else:
        print("Opcion no válida")

    respuesta = input("Desea continuar con la carga de ADN, para otra persona?(S/N)")
    continuar = validacionRespuesta(respuesta)