#creo la matriz
dnaMatriz = []

#pido al usuario ingresar los valores dentro de la matriz
for filas in range(6):
    fila = []
    for columnas in range(6):
        #variable para guardar la letra ingresada (con .upper() convierto a mayúsculas las letras)
        letra = input("Ingrese la letra en la posición ({},{}): ".format(filas + 1,columnas + 1)).upper()

        #agrego la letra ingresada a la fila
        fila.append(letra)
    
    #agrego la fila a la matriz
    dnaMatriz.append(fila)

#muestro la matriz ingresada
print("Matriz ingresada por el usuario")
for row in dnaMatriz:
    print(" ".join(row))

