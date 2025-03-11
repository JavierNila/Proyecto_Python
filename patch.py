import random
from celda import Celda
from nido import Nido

class Patch:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.ambiente = [[Celda() for _ in range(ancho)] for _ in range(alto)]
        self.nidos = {}
