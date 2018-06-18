import pieceA
import pieceB
import piece
import copy

class Checkers():
    def __init__(self):
        self.__table = self.make_table()
        self.__captured_pieces_by_A = 0
        self.__captured_pieces_by_B = 0

    # Funcion: make_table()
    # Parametros: Ninguno
    # Objetivo: Crear el tablero de damas
    # Retorno: Lista con objetos de tipo 'check'
    def make_table(self):
        table = []
        row = 0
        char_in_ascii = 65 #Caracter ascii de la letra 'A'
        while row < 8:
            col = 0
            table.append([])
            while col < 8:
                if (((row + col) % 2) == 0) and (row < 3 or row > 4):
                    char = str(chr(char_in_ascii)) #Convertir un numero a un string
                    if row < 3:
                        fic = pieceB.PieceB(char)
                    else:
                        fic = pieceA.PieceA(char)
                    table[row].append(fic)
                    char_in_ascii += 1
                else:
                    table[row].append('-')
                if row == 3: #Cambiar a minusculas cuando termine con las fichas mayusculas
                    char_in_ascii = 97 #Caracter ascii de la letra 'a'
                col += 1
            row += 1
        return table

    def find_piece(self,target):
        p_row = None
        p_col = None
        row = 0
        while row < 8:
            col = 0
            while col < 8:
                if self.__table[row][col] != '-' and self.__table[row][col].get_mask().find(target) == 0:
                    p_row, p_col = row, col
                    row,col = 8, 8 #Terminar ciclo
                col += 1
            row += 1
        return p_row, p_col

    def move_piece(self, piece, hor_direction, ver_direction):
        row, col = self.find_piece(piece) #Obtener la posicion de la ficha
        result = False
        if row != None and col != None:
            if self.__table[row][col].get_queen():
                if ver_direction == "1":
                    self.pieceA_move(piece, hor_direction)
                else:
                    self.pieceB_move(piece, hor_direction)
            elif isinstance(self.__table[row][col],pieceA.PieceA):
                self.pieceA_move(piece,hor_direction)
                row, col = self.find_piece(piece)
                if row == 0: #Convertir a reina
                    self.__table[row][col].set_queen()
            elif isinstance(self.__table[row][col],pieceB.PieceB):
                self.pieceB_move(piece, hor_direction)
                row, col = self.find_piece(piece)
                if row == 7: #Convertir a reina
                    self.__table[row][col].set_queen()

    def pieceA_move(self, piece, direction):
        row, col = self.find_piece(piece)
        next_col = col - 1 if direction == '1' else col + 1  #Si se mueve a la izquierda o si se mueve a la derecha
        self.eat_pieceA(piece, direction)
        object = self.available_position(row - 1, next_col)
        if object == '-':
            self.__table[row - 1][next_col] = self.__table[row][col]
            self.__table[row][col] = '-'

    def pieceB_move(self, piece, direction):
        row, col = self.find_piece(piece)
        next_col = col - 1 if direction == '1' else col + 1  # Si se mueve a la izquierda o si se mueve a la derecha
        self.eat_pieceB(piece, direction)
        object = self.available_position(row + 1, next_col)
        if object == '-':
            self.__table[row + 1][next_col] = self.__table[row][col]
            self.__table[row][col] = '-'


    def eat_pieceA(self,piece,direction):
        stop = True
        piece_row, piece_col = self.find_piece(piece)
        actual_piece = self.__table[piece_row][piece_col]  # Guardar la pieza en una variable
        if direction == '1': #Si se mueve a la izquierda
            object1 = self.available_position(piece_row-1, piece_col-1)
            object2 = self.available_position(piece_row-2, piece_col-2)
            if (isinstance(actual_piece,pieceA.PieceA) and isinstance(object1, pieceB.PieceB) and object2 == '-') or (actual_piece.get_queen() == True and (type(actual_piece) != type(object1)) and object1 != '-' and object2 == '-'): #Comer ficha del usuario B OR Si es una reina de cualquiera de los dos usuarios, comer ficha del oponente
                self.__table[piece_row-2][piece_col-2] = self.__table[piece_row][piece_col]
                self.__table[piece_row-1][piece_col-1] = '-'
                self.__table[piece_row][piece_col] = '-'
                stop = False
        if direction == '2': #Si se mueve a la derecha
            object1 = self.available_position(piece_row-1, piece_col+1)
            object2 = self.available_position(piece_row-2, piece_col+2)
            if (isinstance(actual_piece,pieceA.PieceA) and isinstance(object1, pieceB.PieceB) and object2 == '-') or (actual_piece.get_queen() == True and (type(actual_piece) != type(object1)) and object1 != '-' and object2 == '-'): #Comer ficha del usuario B OR Si es una reina de cualquiera de los dos usuarios, comer ficha del oponente
                self.__table[piece_row-2][piece_col+2] = self.__table[piece_row][piece_col]
                self.__table[piece_row-1][piece_col+1] = '-'
                self.__table[piece_row][piece_col] = '-'
                stop = False
        if stop:
            return
        self.eat_pieceA(piece,direction)

    def eat_pieceB(self,piece,direction):
        stop = True
        piece_row, piece_col = self.find_piece(piece) #Encontrar la posicion de la pieza
        actual_piece = self.__table[piece_row][piece_col] #Guardar la pieza en una variable
        if direction == '1':  # Si se mueve a la izquierda
            object1 = self.available_position(piece_row + 1, piece_col - 1)
            object2 = self.available_position(piece_row + 2, piece_col - 2)
            if (isinstance(actual_piece,pieceB.PieceB) and isinstance(object1,pieceA.PieceA) and object2 == '-') or (actual_piece.get_queen() == True and (type(actual_piece) != type(object1)) and object1 != '-' and object2 == '-'):  #Comer ficha del usuario B OR Si es una reina de cualquiera de los dos usuarios, comer ficha del oponente
                self.__table[piece_row + 2][piece_col - 2] = self.__table[piece_row][piece_col]
                self.__table[piece_row + 1][piece_col - 1] = '-'
                self.__table[piece_row][piece_col] = '-'
                stop = False
        if direction == '2':  # Si se mueve a la derecha
            object1 = self.available_position(piece_row + 1, piece_col + 1)
            object2 = self.available_position(piece_row + 2, piece_col + 2)
            if (isinstance(actual_piece,pieceB.PieceB) and isinstance(object1,pieceA.PieceA) and object2 == '-') or (actual_piece.get_queen() == True and (type(actual_piece) != type(object1)) and object1 != '-' and object2 == '-'):  #Comer ficha del usuario B OR Si es una reina de cualquiera de los dos usuarios, comer ficha del oponente
                self.__table[piece_row + 2][piece_col + 2] = self.__table[piece_row][piece_col]
                self.__table[piece_row + 1][piece_col + 1] = '-'
                self.__table[piece_row][piece_col] = '-'
                stop = False
        if stop:
            return
        self.eat_pieceB(piece, direction)

    def available_position(self, row, col):
        object = None # Objeto que se encuentra en esa posicion
        if (0 <= row < 8) and (0 <= col < 8):  # Si la posicion a la que se moverá es válida
            object = self.__table[row][col]
        return object

    def check_block(self, turn):
        table_copy = copy.deepcopy(self.__table) #Clonar lista a otra
        for row in self.__table:
            for piece1 in row:
                hor_direction = 1
                while hor_direction <= 2:
                    if isinstance(piece1, piece.Piece):
                        row1, col1 = self.find_piece(piece1.get_mask())
                    if turn == 1 and isinstance(piece1, pieceA.PieceA):  # Si el turno es de las fichas A
                        self.check_block_move_piece(piece1, hor_direction)
                    elif turn == 2 and isinstance(piece1, pieceB.PieceB):
                        self.check_block_move_piece(piece1, hor_direction)
                    result = self.check_move(piece1, row1, col1)
                    hor_direction = (hor_direction + 1) if (result is False) else 3 #Romper el ciclo
        result = self.compare_lists(table_copy)
        self.__table = copy.deepcopy(table_copy)
        return result



    def compare_lists(self, list):
        pos, cont, result = 0, 0, False
        while pos < 8:
            if list[pos] == self.__table[pos]:
                cont += 1
            pos += 1
        if cont == 8:
            result = True
        return result

    #Saber si una ficha se ha movido
    def check_move(self, piece1, row, col):
        result = False
        if isinstance(piece1, piece.Piece):
            row2, col2 = self.find_piece(piece1.get_mask())
            if row != row2 or col != col2:
                result = True
        return result

    def check_block_move_piece(self, piece, hor_direction):
        ver_direction = 1
        if piece.get_queen(): #Si es una reina
            while ver_direction <= 2:
                self.move_piece(piece.get_mask(), ver_direction, hor_direction) #
                ver_direction += 1
        else:
            self.move_piece(piece.get_mask(), hor_direction, 0) #Como no es una reina, no se puede mover verticalmente en cualquier direccion

    def count_pieces(self):
        a_pieces, b_pieces = 0, 0
        for row in self.__table:
            for piece1 in row:
                if isinstance(piece1, pieceA.PieceA):
                    a_pieces += 1
                if isinstance(piece1, pieceB.PieceB):
                    b_pieces += 1
        return a_pieces, b_pieces

    def mandatory_eating(self, turn):
        table_copy = copy.deepcopy(self.__table)  # Clonar lista a otra
        result = False
        ver_direction = 0
        piecesEat = {} #Piezas que pueden comer
        for row in self.__table:
            for piece1 in row:
                hor_direction = 1
                while hor_direction <= 2:
                    if isinstance(piece1, piece.Piece):
                        row1, col1 = self.find_piece(piece1.get_mask())
                        ver_direction = self.mandatory_eating_move_piece(piece1, hor_direction, turn)
                        result = self.check_move(piece1, row1, col1)
                    self.__table = copy.deepcopy(table_copy)
                    if result: #Si el resultado es True es porque la ficha puede comer
                        if piece1.get_queen():
                            piecesEat[piece1.get_mask()[0]] = [str(ver_direction), str(hor_direction)]
                        else:
                            piecesEat[piece1.get_mask()[0]] = [str(hor_direction), str(ver_direction)]
                        result = False
                    hor_direction += 1
        return piecesEat

    def mandatory_eating_move_piece(self, piece1, hor_direction, turn):
        ver_direction = 1
        vertical = 0
        row, col = self.find_piece(piece1.get_mask())
        #La siguiente condicion es para que el codigo solo se ejecute cuando el turno le corresponda a ficha correspondiente
        if (turn == 1 and isinstance(piece1,pieceA.PieceA)) or (turn == 2 and isinstance(piece1,pieceB.PieceB)):
            if piece1.get_queen():
                while ver_direction <= 2:
                    if hor_direction == 1:
                        self.eat_pieceA(piece1.get_mask(), str(ver_direction))
                    else:
                        self.eat_pieceB(piece1.get_mask(), str(ver_direction))
                    result = self.check_move(piece1, row, col)
                    if result:
                        vertical = ver_direction
                        ver_direction = 3 #romper ciclo
                    ver_direction += 1
            else:
                if isinstance(piece1, pieceA.PieceA):
                    self.eat_pieceA(piece1.get_mask(), str(hor_direction))
                elif isinstance(piece1, pieceB.PieceB):
                    self.eat_pieceB(piece1.get_mask(), str(hor_direction))
        return vertical

    def end_game(self):
        result = False
        winner = None
        a_pieces, b_pieces = self.count_pieces()
        self.__captured_pieces_by_A = 12 - b_pieces
        self.__captured_pieces_by_B = 12 - a_pieces
        if a_pieces == 0:
            result = True
            winner = "El ganador es el de las piezas Mayusculas"
        if b_pieces == 0:
            result = True
            winner = " El ganador es el de las piezas Minusculas"
        if a_pieces == 1 and b_pieces == 1:
            result = True
            winner = "Han empatado"
        return result, winner

    def get_table(self):
        return self.__table

    def get_captured_pieces_by_A(self):
        return self.__captured_pieces_by_A

    def get_captured_pieces_by_B(self):
        return self.__captured_pieces_by_B