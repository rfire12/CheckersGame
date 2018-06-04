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
                        fic = pieceA.PieceA(char)
                    else:
                        fic = pieceB.PieceB(char)
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
                if target == self.__table[row][col]:
                    p_row, p_col = row, col
                    row,col = 8 #Terminar ciclo
                col += 1
            row += 1
        return p_row, p_col


    def move_piece(self,piece,direction):
        row, col = self.find_piece(piece) #Obtener la posicion de la ficha
        if isinstance(self.__table[row][col],pieceA):
            self.pieceA_movement(piece,direction)

    def pieceA_movement(self,piece,direction):
        row, col = self.find_piece(piece)
        result = False
        if direction == 1: #Si se mueve hacia la izquierda
            object = self.available_position(row-1 ,col-1)
            if object == '-':
                self.__table[row-1][col-1] = self.__table[row][col]
                self.__table[row][col] = '-'
                result = True
            if isinstance(object,pieceB): #Si lo que se encuentra en esa posicion es una ficha del oponente
                object = self.available_position(row-2, col-2)
                if object == '-':
                    self.__table[row - 2][col - 2] = self.__table[row][col]
                    self.__table[row - 1][col - 1] = '-'
                    self.__table[row][col] = '-'
                    result = True
        return result

    def available_position(self, row, col):
        object = None #Objeto que se encuentra en esa posicion
        if (0 <= row < 8) and (0 <= col < 8):  # Si la posicion a la que se moverá es válida
            object = self.__table[row][col]
        return object

    def get_table(self):
        return self.__table
