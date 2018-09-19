# A saga of inheritance and family names

class Charlemagne:

    def __init__(self):
        self.king = True

    def __str__(self):
        if self.king:
            return "King"
        return "Nope"

class Charles(Charlemagne):

    def __init__(self):

        super().__init__()

    def __str__(self):

        return super() + ' II'


print(str(Charles()))
