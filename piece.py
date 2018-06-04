class Ficha():
    def __init__(self, mask):
        self.mask = mask
        self.type = self.determine_type(mask)

    def __repr__(self):

        return self.mask

    def determine_type(mask):
        type = 2
        if ord(mask) >= 97: #Si el ascii de mask es > a 97 es una letra minuscula
            type = 1
        return type
