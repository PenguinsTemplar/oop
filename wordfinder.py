"""Word Finder: finds random words from a dictionary."""
import random
class WordFinder:
    def __init__(self, dictionary):
        self.words = self.load_words(dictionary)
        print(f"{len(self.words)} words loaded.")
    def load_words(self, dictionary):
        with open(dictionary, 'r') as file:
            return [line.strip() for line in file]
    def random (self):
        return random.choice(self.words)
class SpecialWordFinder(WordFinder):
    def load_words(self, dictionary):
        with open(dictionary, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#') or line.startswith(' ')]