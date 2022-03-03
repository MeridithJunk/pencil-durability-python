class Pencil:

    def __init__(self, durability):
        self.sentence = ""
        self.durability = durability

    def write(self, append):
        self.sentence = self.sentence + append
        return self.sentence
