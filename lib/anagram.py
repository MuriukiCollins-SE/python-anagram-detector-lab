class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        sorted_word = sorted(self.word)
        return [w for w in word_list if sorted(w) == sorted_word]
