class Pencil:

    def __init__(self, durability):
        self.sentence = ""
        self.durability = durability

    def write(self, append):
        for char in append:
            if self.durability > 0:
                if char == " ":
                    self.append_character_on_sentence(char)
                elif char.isupper():
                    self.degradation_and_append_uppercase_letters(char)
                else:
                    self.degradation_and_append_lowercase_letters(char)
        return self.sentence

    def append_character_on_sentence(self, char):
        self.sentence = self.sentence + char

    def degradation_and_append_lowercase_letters(self, char):
        if self.durability > 0:
            self.durability -= 1
            self.append_character_on_sentence(char)

    def degradation_and_append_uppercase_letters(self, char):
        if self.durability > 2:
            self.durability -= 2
            self.append_character_on_sentence(char)
