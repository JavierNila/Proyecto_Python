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

