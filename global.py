#creo clase mutante
class mutante:
    #recibe la matriz
    def __init__(self,dnaMatriz):
        self.dnaMatriz = dnaMatriz

    #agrego el metodo isMutant peido por el ejercicio
    def isMutant(self):
        #guardo el len de la matriz
        n = len(self.dnaMatriz)
        #contador de secuencias iguales
        contador = 0

        #recorro matriz para buscar las letras iguales
        for i in range(n):
            for j in range(n - 3):
                #verifico las horizontales
                if self.secuenciaLetras(self.dnaMatriz[i][j:j+4]):
                    contador += 1

        #si el contador es mayor a uno devuelve True
        return contador > 1

    #verifico si hay 4 letras iguales seguidas        
    def secuenciaLetras(self,secuencia):
        return secuencia.count(secuencia[0]) == 4


def validacionLetra(letra):
    #verifico si la letra es G,C,T,A y si es solamente una sola letra por cada ingreso
    return letra.upper() in ['G','C','A','T'] and len(letra) == 1


#creo la matriz
dnaMatriz = []

#pido al usuario ingresar los valores dentro de la matriz
for filas in range(6):
    fila = []
    for columnas in range(6):
        #variable para guardar la letra ingresada (con .upper() convierto a mayúsculas las letras)
        letra = input("Ingrese la letra en la posición ({},{}), solamente las letras G,C,A,T: ".format(filas + 1,columnas + 1)).upper()

        #valido que la letra ingresada sea la pedida
        while not validacionLetra(letra):
            print("La letra ingresada no corresponde a lo pedido")
            letra = input("Ingrese nuevamente una letra válida(G,C,A,T,), en la posición ({},{}): ".format(filas + 1,columnas + 1)).upper()

        #agrego la letra ingresada a la fila
        fila.append(letra)
    
    #agrego la fila a la matriz
    dnaMatriz.append(fila)

#muestro la matriz ingresada
print("Matriz ingresada por el usuario")
for row in dnaMatriz:
    print(" ".join(row))

#instancio un objeto tipo mutante, le paso la matriz
detector = mutante(dnaMatriz)

#me fijo si la matriz ingresada corresponde a un mutante
esMutante = detector.isMutant()

#muestro si el adn ingresado corresponde o no a un mutante
if esMutante:
    print("El ADN ingresado corresponde a un mutante")
else:
    print("El ADN ingresado NO corresponde a un mutante")