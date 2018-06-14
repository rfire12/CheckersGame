import checkers
import os

tablero = checkers.Checkers()

print("Jugador 1 son las fichas minusculas \n Jugador 2: Mayusculas")
end = False
while end == False:
    for x in tablero.get_table():
        print(*x)
    jug = 1
    print("\nJugador \nIngrese la ficha a mover: ")
    piece = input()
    ver_direction = 0
    if len(piece) == 2:
        print("1-Arriba 2-Abajo")
        ver_direction = input()
    print("1-Izquierda 2-Derecha")
    direction = input()
    tablero.move_piece(piece,direction,ver_direction)
    print('\n' * 5)
    end, winner = tablero.end_game()
    if end == True:
        print("El ganador es el de las piezas " + winner)

