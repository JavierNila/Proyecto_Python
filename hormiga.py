import random
from patch import Patch

# Clase para representar una hormiga
class Hormiga:
    def __init__(self, colonia, energia, patch):
        self.colonia = colonia # Identificador de la colonia a la que pertenece
        self.energia = energia # Energia inicial
        self.tiene_comida = False # Indica si la hormiga lleva comida
        self.viva = True # Indica si la hormiga sigue con vida
        self.posicion = patch.obtener_posicion_nido(colonia) # La hormiga inicia en el nido de su colonia
        self.patch = patch # Entorno en el que se moverá la hormiga

    # Método para que la hormiga busque comida
    def buscar_comida(self):
        if not self.viva: # Verifica si la hormiga está muerta
            return
        x, y = self.posicion # Obtener la posición actual
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) # Dirección aleatoria para moverse
        nueva_x, nueva_y = x + dx, y + dy # Calculo de la nueva posición

        # Verifica si la nueva posición está dentro de los límites del entorno
        if 0 <= nueva_x < self.patch.ancho and 0 <= nueva_y < self.patch.alto:
            nueva_celda = self.patch.ambiente[nueva_y][nueva_x]

            # Verifica si la celda tiene comida
            if nueva_celda.estado == 0:
                nueva_celda.estado = 3 # Marca la celda como vacia
                nueva_celda.energia = 0 # Elimina la energía de la celda
                self.tiene_comida = True # Indica que la hormiga ha recogido comida
                self.energia += 20 # Aumenta la energía de la hormiga al recoger comida
            self.posicion = (nueva_x, nueva_y) # Actualiza la posición
        self.energia -= 1 # Reduce la energía de la hormiga por cada movimiento

        # Si la energia llega a 0, la hormiga muere
        if self.energia <= 0:
            self.viva = False

    # Método para que la hormiga regrese a su nido si tiene comida
    def regresar_al_nido(self):
        if not self.viva or not self.tiene_comida: # Verifica si la hormiga está muerta o no tiene comida
            return
        x, y = self.posicion # Obtener la posición actual
        nido_x, nido_y = self.patch.obtener_posicion_nido(self.colonia)

        # Verifica que el movimiento hacia el nido es de manera secuencial
        if x < nido_x:
            x += 1
        elif x > nido_x:
            x -= 1
        if y < nido_y:
            y += 1
        elif y > nido_y:
            y -= 1

        self.posicion = (x, y) # Actualiza la posición

        # Si la hormiga llego al nido, deposita la comida
        if (x, y) == (nido_x, nido_y):
            self.patch.obtener_nido(self.colonia).almacenar_comida(1)
            self.tiene_comida = False
