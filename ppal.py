# ppal.py
import sys
import random
from var_globals import levels
from mapa import Map
from movimientos import Explorer
from elementos import obtener_elemento

def main():
    print("Bienvenido al juego del Explorador")
    
    # Preguntar por el nivel
    level = input("Elige nivel (facil, rockear, dificil): ").strip().lower()
    if level not in levels:
        print("Nivel no válido. Se usará 'facil' por defecto.")
        level = "facil"
    config = levels[level]
    board_size = config["board_size"]

    # Preguntar por el número de jugadores entre 2 y 5.
    while True:
        try:
            num_players = int(input("¿Cuántos jugadores (entre 2 y 5)? "))
            if 2 <= num_players <= 5:
                break
            else:
                print("El número debe estar entre 2 y 5.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    # Crear el mapa
    game_map = Map(level)

    # Crear la lista de exploradores.
    # Los primeros (num_players - 1) son jugadores humanos, el último será la máquina.
    explorers = []
    for i in range(num_players - 1):
        name = input(f"Nombre del jugador {i+1}: ").strip() or f"Jugador{i+1}"
        explorers.append(Explorer(name, energy=config["max_energia"], start_pos=(0,0)))
    # Agregar el explorador máquina.
    explorers.append(Explorer("Máquina", energy=config["max_energia"], start_pos=(0,0)))

    photographed_animals = [set() for _ in range(num_players)]
    total_animals = config["animales"]

    # Revelar la posición inicial de cada explorador en el mapa
    for ex in explorers:
        game_map.reveal_cell(ex.position[0], ex.position[1])

    turn = 0
    while True:
        current_player = explorers[turn % num_players]
        print("\n" + "="*40)
        print(f"Turno de: {current_player.name}")
        print(f"Energía: {current_player.energy}")
        idx = turn % num_players
        print(f"Animales fotografiados por {current_player.name}: {len(photographed_animals[idx])} de {total_animals}")

        # Mostrar visión antes de moverse
        game_map.display_vision(current_player.position, current_player.vision_pattern)
        
        # Condiciones de fin de juego: Si algún jugador fotografía todos los animales o si solo queda un con energía.
        # Para simplificar, terminamos el juego cuando algún jugador fotografía todos los animales o se queda sin energía.
        if len(photographed_animals[idx]) >= total_animals:
            print(f"¡Felicidades {current_player.name}! Has fotografiado todos los animales.")
            break
        if current_player.energy <= 0:
            print(f"{current_player.name} se ha quedado sin energía.")
            # Si solo queda un jugador con energía, podemos terminar.
            alive = [ex for ex in explorers if ex.energy > 0]
            if len(alive) <= 1:
                print("Fin del juego. Solo queda un jugador con energía.")
                break
            else:
                turn += 1
                continue

        # Para la máquina se escoge un movimiento aleatorio.
        if current_player.name == "Máquina":
            move_cmd = random.choice(['W', 'A', 'S', 'D'])
            print(f"La máquina mueve: {move_cmd}")
        else:
            move_cmd = input("Ingresa dirección (W, A, S, D): ").strip().upper()
            if move_cmd not in ['W', 'A', 'S', 'D']:
                print("Dirección no válida. Se omite el turno.")
                turn += 1
                continue

        prev_position = current_player.position
        # Mover al explorador
        current_player.move(move_cmd, board_size)
        new_i, new_j = current_player.position
        cell = game_map.get_cell(new_i, new_j)

        # Si se intenta atravesar un bosque denso, se revierte el movimiento.
        if cell == "B":
            print("Has chocado con un bosque denso. No puedes atravesarlo. Cambia de dirección.")
            current_player.position = prev_position
            turn += 1
            continue

        # Revelar la casilla actual en el mapa.
        game_map.reveal_cell(new_i, new_j)

        # Aplicar efecto del elemento (usando elementos.py)
        elem = obtener_elemento(cell, config)
        if elem is not None:
            if cell == "A":
                if (new_i, new_j) not in photographed_animals[idx]:
                    elem.aplicar_efecto(current_player, config, photographed=False)
                    photographed_animals[idx].add((new_i, new_j))
                else:
                    elem.aplicar_efecto(current_player, config, photographed=True)
            else:
                elem.aplicar_efecto(current_player, config)
        else:
            print("Movimiento realizado.")

        # Limitar la energía máxima.
        if current_player.energy > config["max_energia"]:
            current_player.energy = config["max_energia"]

        turn += 1

if __name__ == "__main__":
    main()
