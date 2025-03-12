from patch import Patch

if __name__ == "__main__":
    # Crear un ambiente de 30x15
    ambiente = Patch(30, 15)

    # Agregar 40 flores con 50 de energía cada una
    ambiente.agregar_flores(40, 50)

    # Colocar dos nidos en posiciones específicas
    ambiente.colocar_nido(25, 3, 'A')
    ambiente.colocar_nido(4, 11, 'B')

    # Mostrar el estado del ambiente sin hormigas
    ambiente.mostrar_estado([])

