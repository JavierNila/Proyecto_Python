from patch import Patch

if __name__ == "__main__":
    # Crear un ambiente de 20x20
    ambiente = Patch(20, 20)

    # Agregar 40 flores con 50 de energía cada una
    ambiente.agregar_flores(35, 50)

    # Colocar dos nidos en posiciones específicas
    ambiente.colocar_nido(15, 5, 'A')
    ambiente.colocar_nido(3, 15, 'B')

    # Mostrar el estado del ambiente sin hormigas
    ambiente.mostrar_estado([])

