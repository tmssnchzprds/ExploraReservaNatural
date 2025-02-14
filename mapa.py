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
        # Creamos un tablero de estados (revelado o no): inicialmente todas ocultas (False)
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

    def reveal_cell(self, i, j):
        """
        Revela la casilla en la posición (i, j). 
        Se utiliza aritmética modular para asegurar el efecto esférico del tablero.
        """
        i %= self.size
        j %= self.size
        self.revealed[i][j] = True

    def get_cell(self, i, j):
        """Devuelve el contenido de la casilla en (i, j) con envoltura en el tablero."""
        i %= self.size
        j %= self.size
        return self.content[i][j]

    def display_revealed(self):
        """
        Muestra el tablero en la consola. Las casillas reveladas muestran su contenido 
        (o un punto '.' si está vacía) y las no reveladas se representan con '?'.
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
        Muestra en consola las casillas que se pueden ver desde la posición dada, según el patrón de visión.
        Se utiliza la aritmética modular para cubrir los bordes.
        :param position: Tupla (i, j) con la posición del jugador.
        :param vision_pattern: Lista de tuplas (dx, dy) que indican los desplazamientos visibles.
        """
        i0, j0 = position
        print("Visión desde tu posición:")
        for dx, dy in vision_pattern:
            i = (i0 + dx) % self.size
            j = (j0 + dy) % self.size
            content = self.content[i][j] if self.revealed[i][j] or True else "?"  
            # Aquí decidimos mostrar el contenido real para que el jugador vea qué hay en esas casillas.
            print(f"({i0+dx}, {j0+dy}) -> {content}")
        print("-" * 30)

# Ejemplo de uso para pruebas
if __name__ == "__main__":
    # Generamos un mapa para el nivel "facil"
    game_map = Map("facil")
    print("Tablero inicial (todo oculto):")
    game_map.display_revealed()
    
    # Revelamos algunas casillas para ver el contenido
    print("\nRevelamos la casilla (0,0) y (2,3):")
    game_map.reveal_cell(0, 0)
    game_map.reveal_cell(2, 3)
    game_map.display_revealed()
    
    # Mostrar visión desde la posición (2,2) usando el patrón del nivel facil
    print("\nVisión desde (2,2) en nivel facil:")
    game_map.display_vision((2,2), levels["facil"]["vision"])
