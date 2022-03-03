class Pencil:

    def __init__(self, durability):
        self.sentence = ""
        self.durability = durability

    def write(self, append):
        for char in append:
            if self.durability > 0:
                if char.isupper():
                    self.durability -= 2
                    self.sentence = self.sentence + char
                else:
                    self.durability -= 1
                    self.sentence = self.sentence + char
        return self.sentence
