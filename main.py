import checkers
import pieceA
import pieceB


def start():
    end = False
    cont = 0
    turn = 1
    while end is False:
        valid = False
        while valid is False:
            print_table(table)
            mandatory = table.mandatory_eating(turn)
            print("Juegador " + str(turn) + "\nElija la ficha a mover: ")
            piece = input()
            valid = valid_piece(piece, turn, mandatory)
            if valid is True:
                vertical, horizontal = scan(piece)
                if piece in mandatory and (horizontal != mandatory[piece[0]][0] or vertical != mandatory[piece[0]][1]):
                    print("\n!!!!La ficha debe de comer!!!!")
                    valid = False
                else:
                    valid = move(piece, horizontal, vertical)
                    if valid is False:
                        print("!!!!La jugada no es valida!!!!\n")
        print('\n' * 5)
        cont += 1
        if (cont % 2) == 0:
            turn = 1
        else:
            turn = 2
        end, winner = table.end_game()
        if end is False:
            end, winner = block(turn)
    print(winner)


def move(piece, horizontal, vertical):
    row, col = table.find_piece(piece)
    table.move_piece(piece, horizontal, vertical)
    row1, col1 = table.find_piece(piece)
    result = table.check_move(table.get_table()[row1][col1], row, col)
    return result


def block(turn):
    winner = None
    end = False
    if table.check_block(turn):
        if table.get_captured_pieces_by_A() == table.get_captured_pieces_by_B():
            winner = "Han empatado!"
            end = True
        elif table.get_captured_pieces_by_A() == 12:
            winner = "El ganador es el de las piezas minusculas"
            end = True
        else:
            winner = "El ganador es el de las piezas mayusculas"
            end = True
    return end, winner


def scan(piece):
    row, col = table.find_piece(piece)
    if row is not None or col is not None:
        vertical, horizontal = scan_movement(row, col)
    return vertical, horizontal


def scan_movement(row,col):
    vertical, horizontal = '0','0'
    valid = False
    if table.get_table()[row][col].get_queen():
        while valid == False:
            print("1-Arriba 2-Abajo")
            vertical = input()
            if vertical != '1' and vertical != '2':
                print("Movimiento invalido\n")
                valid = False
            else:
                valid = True
        valid = False
    while valid == False:
        print("1-Izquierda 2-Derecha")
        horizontal = input()
        if horizontal != '1' and horizontal != '2':
            print("!!!!Movimiento invalido!!!!\n")
            valid = False
        else:
            valid = True
    return vertical, horizontal


def valid_piece(piece,turn,mandatory):
    result = False
    row, col = table.find_piece(piece)
    if row is None or col is None or piece == '':
        print("\n!!!!Elija una ficha valida!!!!")
    elif turn == 1 and isinstance(table.get_table()[row][col], pieceA.PieceA) == False:
        print("\n!!!!La ficha elejida no le pertenece!!!!")
    elif turn == 2 and isinstance(table.get_table()[row][col], pieceB.PieceB) == False:
        print("\n!!!!La ficha elejida no le pertenece!!!!")
    else:
        result = True

    if len(mandatory) is not 0 and result is True and piece not in mandatory:
        print("\n!!!!Una de las piezas siguientes piezas debe comer: ")
        print(*mandatory.keys())
        print('')
        result = False
    return result


def print_table(table):
    for x in table.get_table():
        print(*x)
    print('\n')

table = checkers.Checkers()
start()
print("Jugador 1 son las fichas minusculas \n Jugador 2: Mayusculas")
