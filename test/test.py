import unittest

from solver.solver import ScrabbleSolver


class ScrabbleSolverValidWordsTest(unittest.TestCase):
    def setUp(self):
        self.solver = ScrabbleSolver('TEST')

    def test_valid_words_returns_list_of_words(self):
        self.assertEqual(list, type(self.solver._valid_words))

    def test_valid_words_contains_correct_words(self):
        self.assertEqual('AA', self.solver._valid_words[0])
        self.assertEqual('ZZZS', self.solver._valid_words[-1])


class ScrabbleSolverGenerateRackTest(unittest.TestCase):
    def test_rack_not_supplied(self):
        with self.assertRaises(ValueError):
            s = ScrabbleSolver()

    def test_rack_supplied_less_than_two(self):
        with self.assertRaises(ValueError):
            s = ScrabbleSolver('A')

    def test_rack_supplied_more_than_fifteen(self):
        with self.assertRaises(ValueError):
            s = ScrabbleSolver('QWERTYUUIOPKHGDDDDDD')

    def test_rack_valid_rack_length(self):
        s = ScrabbleSolver('RULBP')
        self.assertEqual('RULBP', s.rack)

    def test_rack_input_is_string_negative(self):
        with self.assertRaises(ValueError):
            s = ScrabbleSolver(1123)

    def test_rack_is_uppercase(self):
        s = ScrabbleSolver('abcde')
        self.assertEqual('ABCDE', s.rack)


class ScrabbleSolverRackWordListTest(unittest.TestCase):
    def test_no_valid_words_in_rack(self):
        s = ScrabbleSolver('zz')
        s.check_rack_for_valid_words()
        self.assertEqual([], s.valid_rack_words)

    def test_one_valid_word_in_rack(self):
        s = ScrabbleSolver('aa')
        s.check_rack_for_valid_words()
        self.assertEqual(['AA'], s.valid_rack_words)

    def test_multiple_valid_words_in_rack(self):
        s = ScrabbleSolver('set')
        s.check_rack_for_valid_words()
        self.assertEqual(['ES', 'EST', 'ET', 'SET', 'ST', 'TE', 'TES'],
                         s.valid_rack_words)


class ScrabbleSolverHighestScoreTest(unittest.TestCase):
    def test_highest_score_one_option(self):
        s = ScrabbleSolver('aa')
        highest = s.score()
        self.assertEqual('2, aa', highest)

    def test_highest_score_multiple_option(self):
        s = ScrabbleSolver('set')
        highest = s.score()
        self.assertEqual('3, set', highest)

if __name__ == '__main__':
    unittest.main()
