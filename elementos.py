# elementos.py

class Elemento:
    def __init__(self, nombre, simbolo, efecto_energia, descripcion=""):
        """
        Clase base para un elemento del tablero.
        :param nombre: Nombre del elemento.
        :param simbolo: Símbolo que lo representa en el tablero.
        :param efecto_energia: Valor base que afecta la energía al interactuar.
        :param descripcion: Breve descripción del efecto.
        """
        self.nombre = nombre
        self.simbolo = simbolo
        self.efecto_energia = efecto_energia
        self.descripcion = descripcion

    def aplicar_efecto(self, explorer, config, **kwargs):
        """
        Aplica el efecto del elemento al explorador.
        Este método se debe sobrescribir en cada clase derivada.
        """
        pass

class Animal(Elemento):
    def __init__(self, efecto_energia):
        super().__init__("Animal", "A", efecto_energia,
                         "Fotografía a un animal para ganar energía.")
    
    def aplicar_efecto(self, explorer, config, photographed=False):
        if not photographed:
            explorer.energy += config["puntos_animal"]
            print("¡Has fotografiado un animal! Energía ganada:", config["puntos_animal"])
        else:
            print("Este animal ya fue fotografiado.")

class Lago(Elemento):
    def __init__(self, efecto_energia):
        super().__init__("Lago", "L", efecto_energia,
                         "Recupera energía al pasar por un lago.")
    
    def aplicar_efecto(self, explorer, config):
        explorer.energy += config["puntos_lago"]
        print("Has pasado por un lago. Energía ganada:", config["puntos_lago"])

class Trampa(Elemento):
    def __init__(self, efecto_energia):
        super().__init__("Trampa", "T", efecto_energia,
                         "Caer en una trampa reduce tu energía.")
    
    def aplicar_efecto(self, explorer, config):
        explorer.energy += config["puntos_trampa"]
        print("¡Cuidado! Caíste en una trampa. Energía perdida:", -config["puntos_trampa"])

class Refugio(Elemento):
    def __init__(self):
        super().__init__("Refugio", "R", 0,
                         "Recupera toda tu energía al descansar en un refugio.")
    
    def aplicar_efecto(self, explorer, config):
        explorer.energy = config["max_energia"]
        print("Has encontrado un refugio. Energía restaurada al máximo.")

class ReyCazante(Elemento):
    def __init__(self, efecto_energia):
        super().__init__("Rey Cazante", "C", efecto_energia,
                         "El rey cazante reduce tu energía y puede afectar la partida.")
    
    def aplicar_efecto(self, explorer, config):
        explorer.energy += config["puntos_rey"]
        print("Te has encontrado con el rey cazante. Energía perdida:", -config["puntos_rey"])

class BosqueDenso(Elemento):
    def __init__(self):
        super().__init__("Bosque Denso", "B", 0,
                         "Un obstáculo que impide el avance del explorador.")
    
    def aplicar_efecto(self, explorer, config):
        print("Has chocado con un bosque denso. No puedes atravesarlo.")

def obtener_elemento(symbol, config):
    """
    Devuelve una instancia del elemento correspondiente según su símbolo.
    :param symbol: Símbolo del elemento (por ejemplo, 'A', 'L', 'T', 'R', 'C', 'B')
    :param config: Configuración del nivel (para obtener los valores de energía)
    :return: Instancia de la clase correspondiente o None si no hay coincidencia.
    """
    if symbol == "A":
        return Animal(config["puntos_animal"])
    elif symbol == "L":
        return Lago(config["puntos_lago"])
    elif symbol == "T":
        return Trampa(config["puntos_trampa"])
    elif symbol == "R":
        return Refugio()
    elif symbol == "C":
        return ReyCazante(config["puntos_rey"])
    elif symbol == "B":
        return BosqueDenso()
    else:
        return None

# Ejemplo de uso para pruebas:
if __name__ == "__main__":
    # Ejemplo de configuración para el nivel "facil"
    config_facil = {
         "board_size": 5,
         "animales": 2,
         "lagos": 4,
         "trampas": 2,
         "refugios": 2,
         "reyes": 1,
         "puntos_animal": 10,
         "puntos_lago": 5,
         "puntos_trampa": -20,
         "puntos_rey": -30,
         "max_energia": 100,
         "bosques": 2
    }

    # Obtener y probar el efecto de cada elemento
    elementos_simbolos = ["A", "L", "T", "R", "C", "B"]
    for sym in elementos_simbolos:
        elem = obtener_elemento(sym, config_facil)
        print(f"Elemento: {elem.nombre}, Símbolo: {elem.simbolo}, Descripción: {elem.descripcion}")
