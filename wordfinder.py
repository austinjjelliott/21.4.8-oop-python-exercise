import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, path='words.txt'):
        dict_file = open(path)
        self.words = [word.strip() for word in dict_file] #The strip() gets rid of the whitespace and /n characters!
        print(f"{len(self.words)} words read")
    def random(self):
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    def __init__(self, path="words.txt"):
        super().__init__(path)
    def random(self):
        filtered_words = [word for word in self.words if not word.startswith("#")]
        return random.choice(filtered_words)