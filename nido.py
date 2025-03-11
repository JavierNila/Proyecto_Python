# Clase para representar un nido de hormigas en el ambiente
class Nido:
    def __init__(self, colonia, posicion):
        self.colonia = colonia  # Identificador de la colonia ('A' o 'B')
        self.posicion = posicion  # Posición del nido en el entorno (x, y)
        self.comida_almacenada = 0  # Cantidad de comida almacenada en el nido

    def almacenar_comida(self, cantidad):
        self.comida_almacenada += cantidad  # Aumenta la cantidad de comida almacenada

