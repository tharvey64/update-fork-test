import unittest

class TestExerciseOne(unittest.TestCase):
    def test_string_scramble(self):
        tests = [
            dict(test_input=['waffle','aAbBcdeeefgL'],test_output=['a','e','f','l']),
            dict(test_input=['spartacus','billy'],test_output=[]),
            dict(test_input=['string','Scramble'],test_output=['s','r']),
        ]
        for test_values in tests:
            with self.subTest(**test_values):
                self.assertTrue('string_scramble' in globals())
                self.assertIsInstance(string_scramble(*test_values['test_input']), (list, tuple))
                self.assertCountEqual(string_scramble(*test_values['test_input']), test_values['test_output'])