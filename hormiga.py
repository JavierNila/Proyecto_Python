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
        if 0 <= nueva_x < self.patch.ancho and 0 <= nueva_y < self.patch.alto:
            nueva_celda = self.patch.ambiente[nueva_y][nueva_x]
            if nueva_celda.estado == 0:
                nueva_celda.estado = 3
                nueva_celda.energia = 0
                self.tiene_comida = True
                self.energia += 20
            self.posicion = (nueva_x, nueva_y)
        self.energia -= 1
        if self.energia <= 0:
            self.viva = False

    def regresar_al_nido(self):
        if not self.viva or not self.tiene_comida:
            return
        x, y = self.posicion
        nido_x, nido_y = self.patch.obtener_posicion_nido(self.colonia)
        if x < nido_x:
            x += 1
        elif x > nido_x:
            x -= 1
        if y < nido_y:
            y += 1
        elif y > nido_y:
            y -= 1
        self.posicion = (x, y)
