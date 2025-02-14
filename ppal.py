# ppal.py
import sys
from var_globals import levels
from mapa import Map
from movimientos import Explorer
from elementos import obtener_elemento

def main():
    print("Bienvenido al juego del Explorador")
    level = input("Elige nivel (facil, rockear, dificil): ").strip().lower()
    if level not in levels:
        print("Nivel no válido. Se usará 'facil' por defecto.")
        level = "facil"
    config = levels[level]
    board_size = config["board_size"]

    # Crear el mapa y el explorador
    game_map = Map(level)
    explorer = Explorer("Jugador1", energy=config["max_energia"], start_pos=(0, 0))
    photographed_animals = set()
    total_animals = config["animales"]

    # Revelar la posición inicial del explorador en el mapa
    game_map.reveal_cell(explorer.position[0], explorer.position[1])

    while True:
        print("\nEstado del mapa:")
        game_map.display_revealed()
        print("\nEstado del explorador:")
        print(explorer)
        print(f"Animales fotografiados: {len(photographed_animals)} de {total_animals}")
        
        # Condiciones de fin de juego
        if len(photographed_animals) >= total_animals:
            print("¡Felicidades! Has fotografiado todos los animales.")
            break
        if explorer.energy <= 0:
            print("Te has quedado sin energía. Fin del juego.")
            break

        move_cmd = input("Ingresa dirección (W, A, S, D): ").strip().upper()
        if move_cmd not in ['W', 'A', 'S', 'D']:
            print("Dirección no válida. Inténtalo de nuevo.")
            continue

        # Guardamos la posición actual para poder revertirla si se topa con un bosque denso.
        prev_position = explorer.position

        # Mover al explorador
        explorer.move(move_cmd, board_size)
        new_i, new_j = explorer.position
        
        cell = game_map.get_cell(new_i, new_j)
        
        # Si se intenta atravesar un bosque denso, se revierte el movimiento.
        if cell == "B":
            print("Has chocado con un bosque denso. No puedes atravesarlo. Cambia de dirección.")
            explorer.position = prev_position
            continue

        # Revelamos la casilla actual en el mapa.
        game_map.reveal_cell(new_i, new_j)

        # Usamos el módulo elementos.py para obtener y aplicar el efecto del elemento
        elem = obtener_elemento(cell, config)
        if elem is not None:
            if cell == "A":
                # Verificamos si ya se fotografió el animal en esa casilla.
                if (new_i, new_j) not in photographed_animals:
                    elem.aplicar_efecto(explorer, config, photographed=False)
                    photographed_animals.add((new_i, new_j))
                else:
                    elem.aplicar_efecto(explorer, config, photographed=True)
            else:
                elem.aplicar_efecto(explorer, config)
        else:
            print("Movimiento realizado.")

        # Limitar la energía máxima
        if explorer.energy > config["max_energia"]:
            explorer.energy = config["max_energia"]

if __name__ == "__main__":
    main()
