class Piece():
    def __init__(self, mask):
        self.__mask = mask
        self.__type = self.determine_type(mask)

    def __repr__(self):
        return self.__mask

    def determine_type(self,mask):
        type = 2
        if ord(mask) >= 97: #Si el ascii de mask es > a 97 es una letra minuscula
            type = 1
        return type


