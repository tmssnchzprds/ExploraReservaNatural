# var_globals.py

# Configuración de niveles: "facil", "rockear" y "dificil"
levels = {
    "facil": {
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
         "bosques": 2,
         # En el modo fácil: se pueden ver dos casillas en vertical y horizontal y una en diagonales.
         "vision": [(-2,0), (-1,0), (1,0), (2,0),
                    (0,-2), (0,-1), (0,1), (0,2),
                    (-1,-1), (-1,1), (1,-1), (1,1)]
    },
    "rockear": {
         "board_size": 10,
         "animales": 10,
         "lagos": 14,
         "trampas": 10,
         "refugios": 6,
         "reyes": 3,
         "puntos_animal": 5,
         "puntos_lago": 5,
         "puntos_trampa": -25,
         "puntos_rey": -40,
         "max_energia": 50,
         "bosques": 10,
         # Modo rockear: se pueden ver solo las casillas inmediatas (Moore neighborhood)
         "vision": [(-1,0), (1,0), (0,-1), (0,1),
                    (-1,-1), (-1,1), (1,-1), (1,1)]
    },
    "dificil": {
         "board_size": 15,
         "animales": 18,
         "lagos": 20,
         "trampas": 25,
         "refugios": 16,
         "reyes": 5,
         "puntos_animal": 3,
         "puntos_lago": 2,
         "puntos_trampa": -30,
         "puntos_rey": -50,
         "max_energia": 25,
         "bosques": 25,
         # Modo difícil: se ven únicamente las casillas verticales y horizontales inmediatas
         "vision": [(-1,0), (1,0), (0,-1), (0,1)]
    }
}
