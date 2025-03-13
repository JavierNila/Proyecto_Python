import random
from patch import Patch

class Hormiga:
    def __init__(self, colonia, energia, patch):
        self.colonia = colonia
        self.energia = energia
        self.tiene_comida = False
        self.viva = True
        self.posicion = patch.obtener_posicion_nido(colonia)
        self.patch = patch

    def buscar_comida(self):
        if not self.viva:
            return
        x, y = self.posicion
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        nueva_x, nueva_y = x + dx, y + dy
