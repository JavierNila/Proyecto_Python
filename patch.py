import random
from celda import Celda
from nido import Nido

# Clase que representa el entorno donde se mueven las hormigas
class Patch:
    def __init__(self, ancho, alto):
        self.ancho = ancho  # Ancho del entorno
        self.alto = alto  # Alto del entorno
        self.ambiente = [[Celda() for _ in range(ancho)] for _ in range(alto)]  # Matriz de celdas que conforma el entorno
        self.nidos = {}  # Diccionario para almacenar los nidos de cada colonia

    # Método para agregar flores en posiciones aleatorias del entorno
    def agregar_flores(self, num_flores, energia_flor):
        for _ in range(num_flores):
            # Generar coordenadas aleatorias dentro del entorno
            x, y = random.randint(0, self.ancho - 1), random.randint(0, self.alto - 1)
            celda = self.ambiente[y][x]  # Obtener la celda en la posición generada
            
            # Verificar que la celda no contenga un nido y que sea un espacio vacío
            if celda.nido is None and celda.estado == 3:
                celda.estado = 0  # Cambiar estado a flor
                celda.energia = energia_flor  # Asignar la energía de la flor

    # Método para colocar un nido en una posición específica del entorno
    def colocar_nido(self, x, y, colonia):
        celda = self.ambiente[y][x]

        # Asignar el estado de la celda según la colonia (1 = Nido A, 2 = Nido B)
        celda.estado = 1 if colonia == 'A' else 2
        celda.nido = colonia  # Asociar el nido a la celda
        self.nidos[colonia] = Nido(colonia, (x, y))  # Almacenar el nido en el diccionario de nidos
    
    # Método para obtener el nido de una colonia específica
    def obtener_nido(self, colonia):
        return self.nidos.get(colonia)

    # Método para obtener la posición del nido de una colonia
    def obtener_posicion_nido(self, colonia):
        return self.nidos[colonia].posicion if colonia in self.nidos else None

    # Método para mostrar el estado actual del entorno
    def mostrar_estado(self, hormigas):
        # Genera una matriz visual del entorno, inicialmente llena de puntos que representan espacios vacíos
        matriz = [["." for _ in range(self.ancho)] for _ in range(self.alto)]

        # Recorre todas las celdas del entorno para asignar los símbolos correspondientes
        for fila in range(self.alto):
            for columna in range(self.ancho):
                celda = self.ambiente[fila][columna]
                if celda.estado == 0:
                    matriz[fila][columna] = "F"  # "F" representa una flor
                elif celda.estado == 1:
                    matriz[fila][columna] = "A"  # "A" representa un nido de la colonia A
                elif celda.estado == 2:
                    matriz[fila][columna] = "B"  # "B" representa un nido de la colonia B

        # Recorre la lista de hormigas para actualizar su posición
        for hormiga in hormigas:
            if hormiga.viva: # Verifica si la hormiga sigue viva
                x, y = hormiga.posicion # Obtiene la posición actual

                # Representa la hormiga en la matriz con "*" si pertenece a la colonia A, o con "#" si pertenece a la colonia B
                matriz[y][x] = "*" if hormiga.colonia == "A" else "#" 

        # Imprime cada fila de la matriz como una línea de texto 
        for fila in matriz:
            print(" ".join(fila))
        print("\n")

