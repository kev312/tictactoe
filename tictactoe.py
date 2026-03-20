import random
import time

def mostrar_tablero(tablero):
    """Muestra el tablero de juego"""
    print("\n")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
    print("\n")

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador actual ha ganado"""
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    for combo in combinaciones:
        if tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]] == jugador:
            return True
    return False

def obtener_movimiento_ia(tablero, ia_simbolo, jugador_simbolo):
    """IA inteligente: intenta ganar, bloquea, o juega estratégico"""
    casillas_libres = [i for i, x in enumerate(tablero) if x not in ['X', 'O']]
    
    # 1. Intentar ganar si puede
    for casilla in casillas_libres:
        tablero_temp = tablero.copy()
        tablero_temp[casilla] = ia_simbolo
        if verificar_ganador(tablero_temp, ia_simbolo):
            return casilla
    
    # 2. Bloquear al jugador si va a ganar
    for casilla in casillas_libres:
        tablero_temp = tablero.copy()
        tablero_temp[casilla] = jugador_simbolo
        if verificar_ganador(tablero_temp, jugador_simbolo):
            return casilla
    
    # 3. Tomar el centro si está libre
    if 4 in casillas_libres:
        return 4
    
    # 4. Tomar esquinas
    esquinas = [0, 2, 6, 8]
    esquinas_libres = [e for e in esquinas if e in casillas_libres]
    if esquinas_libres:
        return random.choice(esquinas_libres)
    
    # 5. Cualquier casilla libre
    if casillas_libres:
        return random.choice(casillas_libres)
    
    return None

def juego_tres_en_raya():
    """Función principal del juego"""
    print("=" * 40)
    print(" TIC TAC TOE")
    print("=" * 40)
    
    # Configuración del jugador
    nombre = input("\n Introduce tu nombre: ").strip()
    if not nombre:
        nombre = "Jugador"
    
    # Elección de símbolo
    while True:
        simbolo = input(f"{nombre}, ¿quieres ser X o O?: ").upper().strip()
        if simbolo in ['X', 'O']:
            break
        print(" Por favor, elige X u O")
    
    # Asignar símbolos
    jugador_simbolo = simbolo
    ia_simbolo = 'O' if jugador_simbolo == 'X' else 'X'
    
    print(f"\n {nombre} = {jugador_simbolo}")
    print(f" Computadora = {ia_simbolo}")
    
    if jugador_simbolo == 'x':
        print(f"\n {nombre} empiezas primero")
    else:
        print(f"\n La computadora empieza primero")
    
    input("\nPresiona ENTER para comenzar...")
    
    # Inicializar juego
    tablero = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    turno_jugador = (jugador_simbolo == 'X')  # X siempre empieza
    
    while True:
        mostrar_tablero(tablero)
        
        if turno_jugador:
            # Turno del jugador humano
            while True:
                try:
                    posicion = int(input(f"🎮 {nombre}, elige casilla (1-9): ")) - 1
                    
                    if posicion < 0 or posicion > 8:
                        print(" Elige un número entre 1 y 9")
                        continue
                    
                    if tablero[posicion] in ['X', 'O']:
                        print(" Esa casilla ya está ocupada")
                        continue
                    
                    break
                except ValueError:
                    print(" Introduce un número válido")
            
            tablero[posicion] = jugador_simbolo
            
            if verificar_ganador(tablero, jugador_simbolo):
                mostrar_tablero(tablero)
                print(f" ¡Felicidades {nombre}! ¡Has ganado!")
                break
            
        else:
            # Turno de la IA
            print(f" La computadora está pensando...")
            time.sleep(1)  # Pausa dramática
            
            movimiento = obtener_movimiento_ia(tablero, ia_simbolo, jugador_simbolo)
            tablero[movimiento] = ia_simbolo
            print(f" Computadora elige la casilla {movimiento + 1}")
            
            if verificar_ganador(tablero, ia_simbolo):
                mostrar_tablero(tablero)
                print(f" ¡Ha ganado la computadora! Mejor suerte la próxima vez, {nombre}")
                break
        
        # Verificar empate
        if all(casilla in ['X', 'O'] for casilla in tablero):
            mostrar_tablero(tablero)
            print("¡Empate! Buen juego")
            break
        
        turno_jugador = not turno_jugador
    
    # Preguntar si jugar de nuevo
    print("\n" + "=" * 40)
    otra = input("¿Quieres jugar otra vez? (s/n): ").lower().strip()
    if otra == 's':
        juego_tres_en_raya()
    else:
        print(f"\n ¡Hasta luego, {nombre}!")

# Iniciar el juego
if __name__ == "__main__":
    juego_tres_en_raya()