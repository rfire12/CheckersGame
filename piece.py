class Piece():
    def __init__(self, mask):
        self.__mask = mask

    def __repr__(self):
        return self.__mask

    def get_mask(self):
        return self.__mask



