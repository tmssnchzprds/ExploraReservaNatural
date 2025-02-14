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
