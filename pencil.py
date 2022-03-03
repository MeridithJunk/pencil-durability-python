class Pencil:

    def __init__(self, durability):
        self.sentence = ""
        self.durability = durability

    def write(self, append):
        for char in append:
            if self.durability > 0:
                if char == " ":
                    self.sentence = self.sentence + char
                elif char.isupper():
                    self.degradation_uppercase_letters(char)
                else:
                    self.degradation_lowercase_letters(char)
        return self.sentence

    def degradation_lowercase_letters(self, char):
        if self.durability > 0:
            self.durability -= 1
            self.sentence = self.sentence + char

    def degradation_uppercase_letters(self, char):
        if self.durability > 2:
            self.durability -= 2
            self.sentence = self.sentence + char
