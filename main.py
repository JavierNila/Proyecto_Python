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
    
    # Genera una lista de hormigas para ambas colonias
    hormigas = [Hormiga('A', 50, ambiente) for _ in range(10)] # Crea 10 hormigas para la colonia A con 50 unidades de energia. 
    hormigas += [Hormiga('B', 50, ambiente) for _ in range(10)] # Crea 10 hormigas para la colonia B con 50 unidades de energia.

    # Ejecuta la simulación durante 50 ciclos (podemos cambiar el numero de ciclos)
    for ciclo in range(50):
        # Si todas las hormigas están muertas, la simulación se detiene.
        if all(not hormiga.viva for hormiga in hormigas):
            print("Todas las hormigas han muerto. Fin de la simulación.")
            break

        print(f"\nCiclo {ciclo + 1}:") # Muestra el número del ciclo actual.

        # Recorre cada hormiga y ejecuta sus acciones según su estado.
        for hormiga in hormigas:
            # Solo ejecuta acciones si la hormiga sigue viva.
            if hormiga.viva:
                if not hormiga.tiene_comida:
                    hormiga.buscar_comida() # Si no tiene comida, busca una flor.
                else:
                    hormiga.regresar_al_nido() # Si ya tiene comida, regresa al nido.
 
        # Muestra el estado del entorno en la terminal
        ambiente.mostrar_estado(hormigas)

        # Muestra cuánta comida ha almacenado cada colonia
        print(f"Colonia A: Comida almacenada = {ambiente.obtener_nido('A').comida_almacenada}")
        print(f"Colonia B: Comida almacenada = {ambiente.obtener_nido('B').comida_almacenada}")
    
    # Indica que la simulación ha terminado.
    print("Simulación finalizada.")
