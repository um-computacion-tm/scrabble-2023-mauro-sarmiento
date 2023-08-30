import nltk
from nltk.corpus import words

nltk.download('words')

class Dictionary:
    def __init__(self, language='english'):
        self.language = language
        self.valid_words = set(words.words(language))

    def is_valid_word(self, word):
        word = word.lower()
        return word in self.valid_words