function DFS-8-Queens(state, depth)
    if depth == 8
        print(state)
        return True
    
    for each row in 1 to 8
        if no conflict(state, row, depth)
            state[depth] = row
            if DFS-8-Queens(state, depth + 1)
                return True
            state[depth] = 0  // Backtrack

    return False

function no conflict(state, row, depth)
    for each i from 0 to depth - 1
        if state[i] == row or
           state[i] - i == row - depth or
           state[i] + i == row + depth
            return False

    return True




---------------------------------------------

function DFS-8-Queens(state, depth)
    // Si todas las reinas están colocadas, imprime el estado y termina la recursión.
    if depth == 8
        print(state)
        return true

    // Intenta colocar una reina en cada fila de la columna actual.
    for row from 1 to 8
        if no_conflict(state, row, depth)
            state[depth] = row  // Coloca una reina en la posición actual.
            // Llamada recursiva para la siguiente columna.
            if DFS-8-Queens(state, depth + 1)
                return true
            state[depth] = 0  // Backtrack si no se encuentra solución.

    return false

function no_conflict(state, row, depth)
    // Comprueba si la posición de la nueva reina entra en conflicto con las ya colocadas.
    for i from 0 to depth - 1
        // Chequea la misma fila o diagonales.
        if state[i] == row or abs(state[i] - row) == abs(i - depth)
            return false
    return true
