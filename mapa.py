# mapa.py
import random
from var_globals import levels

class Map:
    def __init__(self, level_name):
        if level_name not in levels:
            raise ValueError("Nivel no válido. Usa 'facil', 'rockear' o 'dificil'.")
        self.config = levels[level_name]
        self.size = self.config["board_size"]
        # Creamos el contenido del tablero: inicialmente, cada casilla está vacía (" ")
        self.content = [[" " for _ in range(self.size)] for _ in range(self.size)]
        # Matriz global de celdas reveladas (para acciones globales, por ejemplo, efectos comunes)
        # Se usa para efectos globales, pero cada jugador tiene su propia vista.
        self.revealed = [[False for _ in range(self.size)] for _ in range(self.size)]
        # Colocamos los elementos según la configuración:
        self.place_elements("A", self.config["animales"])
        self.place_elements("L", self.config["lagos"])
        self.place_elements("T", self.config["trampas"])
        self.place_elements("R", self.config["refugios"])
        self.place_elements("C", self.config["reyes"])
        self.place_elements("B", self.config["bosques"])

    def place_elements(self, symbol, count):
        """Coloca de forma aleatoria 'count' elementos con el símbolo 'symbol' en el tablero."""
        placed = 0
        while placed < count:
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            # Solo se coloca si la casilla está vacía
            if self.content[i][j] == " ":
                self.content[i][j] = symbol
                placed += 1

    def reveal_cell_global(self, i, j):
        """Revela la casilla en el mapa global."""
        i %= self.size
        j %= self.size
        self.revealed[i][j] = True

    def get_cell(self, i, j):
        """Devuelve el contenido de la casilla en (i, j) con aritmética modular."""
        i %= self.size
        j %= self.size
        return self.content[i][j]

    def display_revealed(self):
        """
        Muestra el tablero global en la consola. Las casillas reveladas muestran su contenido
        (o '.' si está vacía) y las no reveladas se representan con '?'.
        """
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                if self.revealed[i][j]:
                    cell = self.content[i][j] if self.content[i][j] != " " else "."
                else:
                    cell = "?"
                row += cell + " "
            print(row)

    def display_vision(self, position, vision_pattern):
        """
        Muestra en consola el mapa completo, pero solo muestra el contenido real de las celdas que
        se encuentran en el conjunto de visión del jugador (calculado a partir de vision_pattern)
        y que el jugador ha revelado en su vista personal. El resto se muestra con '?'.
        
        :param position: Tupla (i, j) con la posición del jugador.
        :param vision_pattern: Lista de tuplas (dx, dy) que indican los desplazamientos visibles.
        :param player_revealed: Matriz 2D de booleanos (del mismo tamaño que el mapa) del jugador.
        """
        i0, j0 = position
        # Calcular el conjunto de celdas visibles (globales) a partir del patrón
        visible_set = set()
        for dx, dy in vision_pattern:
            i = (i0 + dx) % self.size
            j = (j0 + dy) % self.size
            visible_set.add((i, j))
        visible_set.add((i0 % self.size, j0 % self.size))
        
        print("Visión desde tu posición:")
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if (i, j) in visible_set:
                    # Si la celda es visible para el jugador y fue revelada por él, mostrar contenido real.
                    cell = self.content[i][j] if (i!=i0 and j!=j0) else "."
                    row.append(cell)
                else:
                    row.append("?")
            print(' '.join(row))
        print("-" * 30)

# Ejemplo de uso para pruebas
if __name__ == "__main__":
    # Generamos un mapa para el nivel "facil"
    game_map = Map("facil")
    print("Tablero global inicial (todo oculto):")
    game_map.display_revealed()
    
    # Revelamos algunas casillas globalmente
    game_map.reveal_cell_global(0, 0)
    game_map.reveal_cell_global(2, 3)
    print("\nTablero global tras revelar algunas casillas:")
    game_map.display_revealed()
    
    # Mostrar visión desde la posición (2,2) usando el patrón del nivel facil
    # Para el ejemplo, creamos una matriz 'revealed' ficticia para el jugador
    player_revealed = [[False for _ in range(game_map.size)] for _ in range(game_map.size)]
    player_revealed[2][2] = True
    player_revealed[0][0] = True
    player_revealed[2][3] = True
    print("\nVisión desde (2,2):")
    game_map.display_vision((2,2), levels["facil"]["vision"], player_revealed)
