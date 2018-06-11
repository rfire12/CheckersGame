import pieceA
import pieceB

class Checkers():
    def __init__(self):
        self.__table = self.make_table()

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
                if self.__table[row][col] != '-' and target == self.__table[row][col].get_mask():
                    p_row, p_col = row, col
                    row,col = 8, 8 #Terminar ciclo
                col += 1
            row += 1
        return p_row, p_col


    def move_piece(self,piece,hor_direction,ver_direction):
        row, col = self.find_piece(piece) #Obtener la posicion de la ficha
        if row != None and col != None:
            if self.__table[row][col].get_queen() == True:
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

    def pieceA_move(self,piece,direction):
        row, col = self.find_piece(piece)
        next_col = col - 1 if direction == '1' else col + 1  #Si se mueve a la izquierda o si se mueve a la derecha
        self.eat_pieceA(piece, direction)
        object = self.available_position(row - 1, next_col)
        if object == '-':
            self.__table[row - 1][next_col] = self.__table[row][col]
            self.__table[row][col] = '-'

    def pieceB_move(self,piece,direction):
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
            if (isinstance(object1, pieceB.PieceB) and object2 == '-') or (actual_piece.get_queen() == True and (type(actual_piece) != type(object1)) and object1 != '-' and object2 == '-'): #Comer ficha del usuario B OR Si es una reina de cualquiera de los dos usuarios, comer ficha del oponente
                self.__table[piece_row-2][piece_col-2] = self.__table[piece_row][piece_col]
                self.__table[piece_row-1][piece_col-1] = '-'
                self.__table[piece_row][piece_col] = '-'
                stop = False
        if direction == '2': #Si se mueve a la derecha
            object1 = self.available_position(piece_row-1, piece_col+1)
            object2 = self.available_position(piece_row-2, piece_col+2)
            if (isinstance(object1, pieceB.PieceB) and object2 == '-') or (actual_piece.get_queen() == True and (type(actual_piece) != type(object1)) and object1 != '-' and object2 == '-'): #Comer ficha del usuario B OR Si es una reina de cualquiera de los dos usuarios, comer ficha del oponente
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
            if (isinstance(object1,pieceA.PieceA) and object2 == '-') or (actual_piece.get_queen() == True and (type(actual_piece) != type(object1)) and object1 != '-' and object2 == '-'):  #Comer ficha del usuario B OR Si es una reina de cualquiera de los dos usuarios, comer ficha del oponente
                self.__table[piece_row + 2][piece_col - 2] = self.__table[piece_row][piece_col]
                self.__table[piece_row + 1][piece_col - 1] = '-'
                self.__table[piece_row][piece_col] = '-'
                stop = False
        if direction == '2':  # Si se mueve a la derecha
            object1 = self.available_position(piece_row + 1, piece_col + 1)
            object2 = self.available_position(piece_row + 2, piece_col + 2)
            if (isinstance(object1,pieceA.PieceA) and object2 == '-') or (actual_piece.get_queen() == True and (type(actual_piece) != type(object1)) and object1 != '-' and object2 == '-'):  #Comer ficha del usuario B OR Si es una reina de cualquiera de los dos usuarios, comer ficha del oponente
                self.__table[piece_row + 2][piece_col + 2] = self.__table[piece_row][piece_col]
                self.__table[piece_row + 1][piece_col + 1] = '-'
                self.__table[piece_row][piece_col] = '-'
                stop = False
        if stop:
            return
        self.eat_pieceB(piece, direction)


    def available_position(self, row, col):
        object = None #Objeto que se encuentra en esa posicion
        if (0 <= row < 8) and (0 <= col < 8):  # Si la posicion a la que se moverá es válida
            object = self.__table[row][col]
        return object

    def get_table(self):
        return self.__table
