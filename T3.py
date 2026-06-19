laberinto = [
    [1,  1,  1,  1,  0,  1,  1,  1,  1],   # F
    [-2, 0,  0, -1,  0,  1,  0,  1,  0],
    [1,  1,  0,  1,  1,  1,  0,  1,  0],
    [0,  1,  0, -1,  0,  0,  0, -1,  0],
    [1,  1,  1,  1,  1,  1,  1,  1,  0],
    [-1, 0,  0,  0,  0,  0,  0,  1,  1],
    [1,  1,  1,  1, -1,  1,  1,  1,  0],
    [1,  0,  0,  1,  0,  1,  0,  1,  0],
    [1,  1, -1,  1,  1,  1,  0,  1,  1]    # I
]

FILAS = len(laberinto)
COLUMNAS = len(laberinto[0])

INICIO = (8, 0)
FIN = (0, 0)

VIDAS_INICIALES = 3

MOVIMIENTOS = [
    (1, 0, "ABAJO"),
    (0, 1, "DERECHA"),
    (-1, 0, "ARRIBA"),
    (0, -1, "IZQUIERDA")
]

visitado = [[False] * COLUMNAS for _ in range(FILAS)]
camino = []
contador_pasos = 1

def es_valido(fila, columna):
    return (
        0 <= fila < FILAS and
        0 <= columna < COLUMNAS
    )

def backtracking(fila, columna, vidas):

    global contador_pasos
    if not es_valido(fila, columna):
        return False
    if visitado[fila][columna]:
        return False
    if laberinto[fila][columna] == 0:
        return False
    vidas_actuales = vidas
    if (fila, columna) != INICIO:
        if laberinto[fila][columna] == -1:
            vidas_actuales -= 1
        elif laberinto[fila][columna] == -2:
            vidas_actuales -= 2
    if vidas_actuales <= 0:
        return False
    visitado[fila][columna] = True
    camino.append((fila, columna))

    print(
        f"Paso {contador_pasos}: "
        f"({fila},{columna}) "
        f"Valor={laberinto[fila][columna]} "
        f"Vidas={vidas_actuales}"
    )

    contador_pasos += 1

    if (fila, columna) == FIN:
        return True
    for df, dc, direccion in MOVIMIENTOS:
        nueva_fila = fila + df
        nueva_columna = columna + dc
        if backtracking(
            nueva_fila,
            nueva_columna,
            vidas_actuales
        ):
            return True
    print(
        f"Retrocediendo desde "
        f"({fila},{columna})"
    )

    camino.pop()
    visitado[fila][columna] = False

    return False

print("=" * 70)
print("LABERINTO ORIGINAL")
print("=" * 70)

for i in range(FILAS):
    fila_visual = []
    for j in range(COLUMNAS):
        if (i, j) == FIN:
            fila_visual.append("F")
        elif (i, j) == INICIO:
            fila_visual.append("I")
        else:
            fila_visual.append(str(laberinto[i][j]))
    print(" ".join(f"{x:>3}" for x in fila_visual))
print()

encontrado = backtracking(
    INICIO[0],
    INICIO[1],
    VIDAS_INICIALES
)

print("\n" + "=" * 70)

if encontrado:
    print("RESULTADO: SALIDA ENCONTRADA")
    print("\nCAMINO FINAL:")
    for posicion in camino:
        print(posicion)
    matriz_solucion = [
        [0] * COLUMNAS
        for _ in range(FILAS)
    ]

    for fila, columna in camino:
        matriz_solucion[fila][columna] = 1
    print("\nMATRIZ SOLUCIÓN\n")
    for fila in matriz_solucion:
        print(fila)

    print("\nCAMINO DIBUJADO CON *\n")
    dibujo = []
    for i in range(FILAS):
        fila_dibujo = []
        for j in range(COLUMNAS):
            if (i, j) == FIN:
                fila_dibujo.append("F")
            elif (i, j) == INICIO:
                fila_dibujo.append("I")
            elif (i, j) in camino:
                fila_dibujo.append("*")
            elif laberinto[i][j] == 0:
                fila_dibujo.append("■")
            else:
                fila_dibujo.append("·")
        dibujo.append(fila_dibujo)
    for fila in dibujo:
        print(" ".join(fila))
else:
    print("RESULTADO: NO EXISTE CAMINO VÁLIDO")
print("=" * 70)