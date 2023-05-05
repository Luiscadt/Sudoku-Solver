## Sudoku Solver

Sudoku is a fun and challenging game that requires logic and critical thinking. This code is a Python program that solves a Sudoku puzzle using a recursive backtracking algorithm. The program is based on a 9 x 9 grid, where each cell can contain a number from 1 to 9.

The Sudoku puzzle is represented as a two-dimensional list called `sudoku`. The puzzle is initially filled with some numbers and some empty cells, represented by the value `0`. The `print_sudoku` function prints the Sudoku puzzle on the screen.

The `obtener_coordenadas_grid` and `obtener_grid_para_celda` functions are used to extract the subgrid of 3 x 3 cells that corresponds to a given cell in the Sudoku grid.

The `es_posible` function checks whether it is possible to fill a given cell with a given value, based on the current state of the Sudoku grid. It checks if the value is already present in the same row, same column, or same subgrid.

The `resolver_sudoku` function uses a recursive backtracking algorithm to fill in the empty cells of the Sudoku grid. It starts by iterating over each cell of the grid. If the cell is empty (i.e., its value is `0`), the function tries to fill it with each possible value from 1 to 9, one at a time. If a value is found that does not violate the rules of Sudoku, the function recursively calls itself to fill in the next empty cell. If no value can be found that satisfies the rules of Sudoku, the function backtracks to the previous cell and tries a different value. If the function reaches the end of the grid, it prints the solved Sudoku puzzle on the screen.

To use this code, you can copy and paste it into a Python environment, and run the `resolver_sudoku` function with the Sudoku puzzle you want to solve. The solved Sudoku puzzle will be printed on the screen.

## Resolvedor de Sudoku

El Sudoku es un juego divertido y desafiante que requiere lógica y pensamiento crítico. Este código es un programa en Python que resuelve un rompecabezas de Sudoku usando un algoritmo de retroceso recursivo. El programa se basa en una cuadrícula de 9 x 9, donde cada celda puede contener un número del 1 al 9.

El rompecabezas de Sudoku se representa como una lista bidimensional llamada `sudoku`. El rompecabezas está inicialmente lleno de algunos números y algunas celdas vacías, representadas por el valor `0`. La función `print_sudoku` imprime el rompecabezas de Sudoku en la pantalla.

Las funciones `obtener_coordenadas_grid` y `obtener_grid_para_celda` se utilizan para extraer la subcuadrícula de 3 x 3 celdas que corresponde a una celda dada en la cuadrícula de Sudoku.

La función `es_posible` verifica si es posible llenar una celda dada con un valor dado, según el estado actual de la cuadrícula de Sudoku. Verifica si el valor ya está presente en la misma fila, misma columna o misma subcuadrícula.

La función `resolver_sudoku` utiliza un algoritmo de retroceso recursivo para llenar las celdas vacías de la cuadrícula de Sudoku. Comienza iterando sobre cada celda de la cuadrícula. Si la celda está vacía (es decir, su valor es `0`), la función intenta llenarla con cada valor posible del 1 al 9, uno a la vez. Si se encuentra un valor que no viola las reglas del Sudoku, la función llama recursivamente a sí misma para llenar la siguiente celda vacía. Si no se puede encontrar ningún valor que satisfaga las reglas del Sudoku, la función retrocede a la celda anterior y prueba un valor diferente. Si la función llega al final de la cuadrícula, imprime el rompecabezas de Sudoku resuelto en la pantalla.

Para usar este código, puedes copiar y pegarlo en un entorno de Python y ejecutar la función `resolver_sudoku` con el rompecabezas de Sudoku que deseas resolver. El rompecabezas de Sudoku resuelto se imprimirá en la pantalla.