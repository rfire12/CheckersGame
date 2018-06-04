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

    def find_piece(self,target,table):
        p_row = None
        p_col = None
        row = 0
        while row < 8:
            col = 0
            while col < 8:
                if target == table[row][col]:
                    p_row, p_col = row, col
                    row,col = 8 #Terminar ciclo
                col += 1
            row += 1
        return p_row, p_col

    def get_table(self):
        return self.__table
