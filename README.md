# Proyecto_Python

## Simulacion de Hormiguero
Se busca diseñar e implementar una simulacion de colonias de hormigas, el proposito es modelar el comportamiento de las hormigas mientras buscan comida y la llevan a su respectivo nido, tomando en cuenta factores como la energia, ubicacion de los recursos y las decisiones de cada hormiga.

## Funcionalidad 
- **Generacion del entorno**: Se crea una cuadricula donde se distribuyen flores como fuente de alimento y nidos para cada colonia.
- **Visualizacion del entorno**: Se representa el estado actual del ambiente, mostrando la ubicacion de los nidos, flores y hormigas
- **Movimiento de las hormigas**: Las hormigas salen de su nido, buscan comida y la transportan de vuelta.
- **Gestion de energia**: Cada hormiga tiene una cantidad de energia limitada, la cual disminuye con cada movimiento.

## Interaccion del Usuario
El usuario no interactua directamente con la simulacion, ya que esta corre de manera automatica. Sin embargo, puede modificar parametros en el codigo (main.py) como:
- **Tamaño del entorno**.
- **Cantidad y energia de las flores**.
- **Cantidad de hormigas**.
- **Numero de ciclos de la simulacion**.
