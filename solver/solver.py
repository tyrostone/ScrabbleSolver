import sys


class ScrabbleSolver(object):
    SCORED_LETTERS = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                      "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                      "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                      "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                      "x": 8, "z": 10}

    @staticmethod
    def _open_words_file(file_):
        with open(file_, 'r+') as f:
            words = [x.strip() for x in f.readlines()]
            return words

    @staticmethod
    def _generate_rack(rack=None):
        if rack is None or type(rack) is not str or len(rack) < 2 or len(rack) > 15:
            raise ValueError(
                "You must supply between 2 and 15 letters to create a rack")
            sys.exit(1)
        return rack.upper()

    @staticmethod
    def _calculate_score(word):
        total = 0
        for letter in word:
            total += ScrabbleSolver.SCORED_LETTERS[letter.lower()]
        return total

    @staticmethod
    def _get_max_of_word_scores(scores):
        return max(scores.iterkeys(), key=(lambda key: scores[key]))

    def __init__(self, rack=None):
        self._valid_words = self._open_words_file('sowpods.txt')
        self._rack = self._generate_rack(rack)
        self._valid_rack_words = []

    def score(self):
        self.check_rack_for_valid_words()
        highest = self.get_highest_scoring_valid_word()
        return highest

    @property
    def rack(self):
        return self._rack

    @property
    def valid_rack_words(self):
        return self._valid_rack_words

    def check_rack_for_valid_words(self):
        for word in self._valid_words:
            temp_rack = list(self.rack[:])
            counter = 0
            for letter in word:
                if letter in temp_rack:
                    index = temp_rack.index(letter)
                    temp_rack.pop(index)
                    counter += 1
            if len(word) == counter:
                self._valid_rack_words.append(word)

    def get_highest_scoring_valid_word(self):
        word_scores = {}
        for word in self.valid_rack_words:
            word_scores[word] = ScrabbleSolver._calculate_score(word)
        highest_scoring_word = ScrabbleSolver._get_max_of_word_scores(
            word_scores)
        self.highest_scoring_word = str((word_scores[highest_scoring_word],
                                         highest_scoring_word.lower()))
        return "{}, {}".format(word_scores[highest_scoring_word],
                               highest_scoring_word.lower())
