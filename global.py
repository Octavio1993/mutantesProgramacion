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
            print("La letr ingresada no corresponde a lo pedido")
            letra = input("Ingrese nuevamente una letra válida(G,C,A,T,), en la posición ({},{}): ".format(filas + 1,columnas + 1)).upper()

        #agrego la letra ingresada a la fila
        fila.append(letra)
    
    #agrego la fila a la matriz
    dnaMatriz.append(fila)

#muestro la matriz ingresada
print("Matriz ingresada por el usuario")
for row in dnaMatriz:
    print(" ".join(row))

