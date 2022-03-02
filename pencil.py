class Pencil:

    def __init__(self):
        self.sentence = ""

    def write(self, append):
        self.sentence = self.sentence + append
        return self.sentence
