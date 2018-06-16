import checkers
import os

tablero = checkers.Checkers()

print("Jugador 1 son las fichas minusculas \n Jugador 2: Mayusculas")
end = False
cont = 0
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

    if (cont % 2) == 0:
        turn = 1
    else:
        turn = 2
    cont += 1
    if end == True:
        print(winner)

    if tablero.check_block(turn):
        if tablero.get_captured_pieces_by_A() == tablero.get_captured_pieces_by_B():
            print("Han empatado!")
        elif tablero.get_captured_pieces_by_A() == 12:
            print("El ganador es el de las piezas minusculas")
        else:
            print("El ganador es el de las piezas mayusculas")