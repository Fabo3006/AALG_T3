# Problema 1 - T3

## Análisis de Algoritmos y Estrategias de Programación

### CARLOS FABIAN QUISPE LEON - 226413.15103 - 19/06/2026

Se tiene un laberinto representado mediante una matriz de 9x9, el ratón inicia en la esquina inferior izquierda (I) y debe llegar a la esquina superior izquierda (F).

Tenemos que, las celdas con valor:

- 1 permiten el paso normal.
- -1 restan una vida.
- -2 restan dos vidas.
- 0 representan obstáculos.

El ratón dispone inicialmente de 3 vidas.

Un camino es considerado inválido cuando las vidas llegan a 0. Para resolver el problema se utilizó la técnica de Backtracking. El algoritmo explora recursivamente los caminos posibles siguiendo el orden:

1. Abajo
2. Derecha
3. Arriba
4. Izquierda

Cuando una ruta no permite llegar a la salida, el algoritmo retrocede y prueba una alternativa.
