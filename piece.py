class Piece(object):
    def __init__(self, mask):
        self.__mask = mask
        self.__queen = False
        self.__posX = None
        self.__posY = None

    def __repr__(self):
        return self.__mask

    def get_mask(self):
        return self.__mask

    def set_mask(self):
        self.__mask = self.__mask + '+'

    def get_queen(self):
        return self.__queen

    def set_queen(self):
        self.__queen = True
        self.set_mask()

    def set_pos_x(self, posX):
        self.__posX = posX

    def set_pos_y(self, posY):
        self.__posY = posY

    def get_pos_x(self):
        return self.__posX

    def get_pos_y(self):
        return self.__posY



