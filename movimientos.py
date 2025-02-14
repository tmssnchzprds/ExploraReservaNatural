# movimientos.py

class Explorer:
    def __init__(self, name, energy, start_pos=(0, 0)):
        """
        Inicializa un explorador con un nombre, una cantidad de energía y una posición inicial.
        :param name: Nombre del explorador.
        :param energy: Energía inicial del explorador.
        :param start_pos: Tupla (fila, columna) de la posición inicial.
        """
        self.name = name
        self.energy = energy
        self.position = start_pos  # (fila, columna)

    def move(self, direction, board_size):
        """
        Mueve al explorador una casilla en la dirección indicada, con efecto de "envoltura" en el tablero.
        Las direcciones válidas son:
            - 'W': arriba (fila - 1)
            - 'S': abajo (fila + 1)
            - 'A': izquierda (columna - 1)
            - 'D': derecha (columna + 1)
        Se actualiza la posición del explorador aplicando aritmética modular.
        :param direction: Cadena con la dirección ('W', 'A', 'S', 'D')
        :param board_size: Tamaño del tablero (número de filas o columnas, se asume tablero cuadrado)
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

    def __str__(self):
        return f"Explorer {self.name}: Posición {self.position}, Energía {self.energy}"

# Ejemplo de uso para pruebas
if __name__ == "__main__":
    board_size = 5  # Ejemplo de un tablero de 5x5 (puede venir de var_globals en el juego)
    explorer = Explorer("Jugador1", energy=100, start_pos=(0, 0))
    print("Estado inicial:")
    print(explorer)
    
    # Simulación de movimientos
    movimientos = ['W', 'D', 'S', 'A', 'S']
    for move_cmd in movimientos:
        explorer.move(move_cmd, board_size)
        print(f"Después de mover {move_cmd}: {explorer}")
