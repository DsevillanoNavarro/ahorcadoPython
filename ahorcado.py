import random
fallos = 0  
print("1) 1 Jugador ")
print("2) 2 Jugadores ")
numJugadores = int(input())

def palabra_aleatoria():
    numero_aleatorio = random.randint(1, 100)
    
    with open('palabras.txt', 'r') as archivo:
        lineas = archivo.readlines()
        palabra = lineas[numero_aleatorio - 1].strip()
        return palabra

def guionesJuegoPrimero(palabraGuiones):
    guiones = ""
    for _ in range(len(palabraGuiones)):
        guiones += "_"
    print("        "+guiones)


def mostrarAhorcado(errores):
    print("\033[H\033[J", end="")
    etapas = [
        """
           ------
           |    |
                |
                |
                |
                |
                |
        =========
        """,  # 0 errores
        """
           ------
           |    |
           O    |
                |
                |
                |
                |
        =========
        """,  # 1 error
        """
           ------
           |    |
           O    |
           |    |
                |
                |
                |
        =========
        """,  # 2 errores
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
                |
        =========
        """,  # 3 errores
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |return 
                |
                |
        =========
        """,  # 5 errores
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
                |
        =========
        """,  # 6 errores - ¡Juego terminado!
    ]
    
    print (etapas[errores])
 
def encontrar_letra(palabra,letra):
    global fallos
    cantidadAcertada = len(letrasAcertadas)
    for indice, caracter in enumerate(palabra):
        
        if caracter == letra and caracter not in letrasAcertadas:
            letrasAcertadas.append(indice) 
    if len(letrasAcertadas) == cantidadAcertada:
        fallos += 1
        
        
def calcularGuiones():
    texto = list(palabra)
    for indice in range(len(texto)):
        
        if indice not in letrasAcertadas:  
            texto[indice] = "_"
    texto_cadena = "".join(texto)
    print(texto_cadena)
    
    
if numJugadores == 1:
    palabra = str(palabra_aleatoria())
else:
    palabra = str(input("Dime una palabra para ponerle a tu compañero: "))
letrasAcertadas = []
mostrarAhorcado(fallos)
guionesJuegoPrimero(palabra)
encontrar_letra(palabra,str(input("Digame una letra: ")))

while fallos < 6 and len(letrasAcertadas) != len(palabra):
    mostrarAhorcado(fallos)
    calcularGuiones()
    print("TIENES "+str(fallos)+" FALLOS")
    encontrar_letra(palabra,str(input("Digame una letra: ")))
    
if fallos == 6:
    print("HAS PERDIDO TIENES 6 FALLOS")
    print("LA PALABRA ERA: "+ palabra)
else:
    print("GANASTE")