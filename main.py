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
    print("1-Izquierda 2-Derecha")
    direction = input()
    tablero.move_piece(piece,direction)
    print('\n' * 5)
