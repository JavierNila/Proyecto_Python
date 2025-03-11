# Clase para representar cada celda del ambiente
class Celda:
    def __init__(self):
        self.estado = 3  # Estado inicial (3 = piso vacío)
        self.energia = 0  # Energía asociada a la celda
        self.nido = None  # Identificador del nido presente en la celda
