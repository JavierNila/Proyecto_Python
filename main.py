from patch import Patch
from hormiga import Hormiga

if __name__ == "__main__":
    # Crear un ambiente de 30x15
    ambiente = Patch(30, 15)

    # Agregar 40 flores con 50 de energía cada una
    ambiente.agregar_flores(40, 50)

    # Colocar dos nidos en posiciones específicas
    ambiente.colocar_nido(25, 3, 'A')
    ambiente.colocar_nido(4, 11, 'B')

    hormigas = [Hormiga('A', 50, ambiente) for _ in range(10)] 
    hormigas += [Hormiga('B', 50, ambiente) for _ in range(10)]

    for ciclo in range(50):
        if all(not hormiga.viva for hormiga in hormigas):
            print("Todas las hormigas han muerto. Fin de la simulación.")
            break
        print(f"\nCiclo {ciclo + 1}:")
        for hormiga in hormigas:
            if hormiga.viva:
                if not hormiga.tiene_comida:
                    hormiga.buscar_comida()
                else:
                    hormiga.regresar_al_nido()
        ambiente.mostrar_estado(hormigas)
        print(f"Colonia A: Comida almacenada = {ambiente.obtener_nido('A').comida_almacenada}")
        print(f"Colonia B: Comida almacenada = {ambiente.obtener_nido('B').comida_almacenada}")
    
    print("Simulación finalizada.")
