class Piece(object):
    def __init__(self, mask):
        self.__mask = mask
        self.__queen = False

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



