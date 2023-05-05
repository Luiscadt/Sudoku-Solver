# Resolvedor de Sudoku

sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def print_sudoku(sudoku):
    for l in sudoku:
        print(l)

def obtener_coordenadas_grid(val):
    if val <= 2:
        return 0
    elif val > 2 and  val <= 5:
        return 1
    elif val > 5 and val <= 8:
        return 2

def obtener_grid_para_celda(x, y, sudoku):
    subgrid_col = obtener_coordenadas_grid(x)
    subgrid_fila = obtener_coordenadas_grid(y)
    
    grid = []

    for fila in sudoku[subgrid_fila * 3 : subgrid_fila * 3 + 3]:
        for celda in fila[subgrid_col * 3 : subgrid_col * 3 + 3]:
            grid.append(celda)
    return grid

def es_posible(x, y, valor, sudoku):
    # Revisar la fila

    if valor in sudoku[y]:
        return False
    
    # Revisar la columna

    col = [fila[x] for fila in sudoku]
    # print (col)
    if valor in col:
        return False

    #Revisar sub grid 3 x 3

    grid3x3 = obtener_grid_para_celda(x, y, sudoku)
    if valor in grid3x3:
        return False

    return True


def resolver_sudoku(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for valor in range(1,10):
                    if es_posible(x, y, valor, sudoku):
                        sudoku[y][x] = valor
                        resolver_sudoku(sudoku)      
                        sudoku[y][x] = 0
                return
    print_sudoku(sudoku)
    return
                    
resolver_sudoku(sudoku)
# print_sudoku(sudoku)
# es_posible(6, 8, 1 ,sudoku)