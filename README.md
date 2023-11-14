
> # ***mutantesProgramacion***

    * Octavio Nicolas Ragusa
    * DNI: 36850596
    * email: onragusa93@gmail.com

> ## De que va el proyecto

* Este proyecto creado en Python va a detectar, a través de la secuencia de ADN ingresada, si una persona es mutante o no.

> ## Como se resolvió el proyecto

* **Ingresa la secuencia de ADN**
    
    * Usuario ingresa la secuencia de ADN, usando las letras G,C,A,T para crear la matriz. A través de la función crearMatriz(). La cual pide las letras, y las guarda dentro de la matriz, devolviendo la matriz llena.

    ```bash
    #creo la matriz
    dnaMatriz = ingresarMatriz()
    ```

    * Se verifica que las letras ingresadas sean las pedidas por el programa, antes de guardarlas en la matriz. A través del método validacionLetra()

    ```bash
    def validacionLetra(letra):
    #verifico si la letra es G,C,T,A y si es solamente una sola letra por cada ingreso
    return letra.upper() in ['G','C','A','T'] and len(letra) == 1
    ```

* **Detección de Mutantes:**

    * A través del algoritmo, el programa recorre la matriz buscando secuencias de cuatro letras iguales, en forma horizontal, vertical y/o diagonal.

    * Determina si la secuencia ingresada corresponde o no a un mutante.

* **Resultado**

    * El programa muestra por pantalla si la secuencia ingresada corresponde a un mutante o no.

* **Continuación del programa:**

    * Se pregunta al usuario si desea o no seguir con la carga de una nueva matriz.

> ### Como correrlo

* **Enlace para clonar el repositorio**
    
    * https://github.com/Octavio1993/mutantesProgramacion.git

* Ingresar al directorio del proyecto y ejecutar el programa (VSCode):
``` bash
python global.py

```
* Seguir las instrucciones en la consola para ingresar los datos pedidos:
```bash
"Ingrese la letra en la posición ({},{}), solamente las letras G,C,A,T: "
```

* Parte del algoritmo de búsqueda:
```bash
#recorro matriz para buscar las letras iguales
        for i in range(n):
            for j in range(n - 3):
                #verifico las horizontales
                secHorizontal = self.dnaMatriz[i][j:j + 4]
                if self.secuencia(secHorizontal):
                    contador += 1
                    if contador > 1:
                        return True
```

* Resultado de la búsqueda

```bash
 #muestro si el adn ingresado corresponde o no a un mutante
    if esMutante:
        print("El ADN ingresado corresponde a un mutante")
    else:
        print("El ADN ingresado NO corresponde a un mutante")
```

* Continuación del programa

```bash
"Desea continuar con la carga de ADN, para otra persona?(S/N)"
```