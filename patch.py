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

