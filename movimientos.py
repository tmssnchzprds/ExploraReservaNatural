# movimientos.py
import random

class Explorer:
    def __init__(self, name, energy, board_size, start_pos=None):
        """
        Inicializa un explorador con un nombre, energía y posición aleatoria (o especificada).
        Además, crea una matriz 'revealed' para almacenar las celdas que este jugador ha visto.
        """
        self.name = name
        self.energy = energy
        self.board_size = board_size
        if start_pos is None:
            self.position = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
        else:
            self.position = start_pos
        # Matriz de celdas reveladas para este jugador (inicialmente todas False)
        self.revealed = [[False for _ in range(board_size)] for _ in range(board_size)]
        # Revelamos la casilla inicial para este jugador
        i, j = self.position
        self.revealed[i][j] = True

    def move(self, direction, board_size):
        """
        Mueve al explorador una casilla en la dirección indicada, con efecto esférico.
        Direcciones válidas: 'W', 'A', 'S', 'D'.
        """
        i, j = self.position
        if direction.upper() == 'W':
            i = (i - 1) % board_size
        elif direction.upper() == 'S':
            i = (i + 1) % board_size
        elif direction.upper() == 'A':
            j = (j - 1) % board_size
        elif direction.upper() == 'D':
            j = (j + 1) % board_size
        else:
            raise ValueError("Dirección no válida. Usa 'W', 'A', 'S' o 'D'.")
        self.position = (i, j)
        # Al moverse, se revela la nueva casilla en su propio mapa
        self.revealed[i][j] = True

    def __str__(self):
        return f"Explorer {self.name}: Posición {self.position}, Energía {self.energy}"

