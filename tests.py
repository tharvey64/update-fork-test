import unittest

class TestExerciseOne(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        self.assertTrue('fahrenheit_to_celsius' in globals())
        tests = [
            dict(test_input=10,test_output=-12.22), 
            dict(test_input=75,test_output=23.88), 
            dict(test_input=245,test_output=118.33)
        ]
        for test_values in tests:
            with self.subTest(**test_values):
                self.assertIsInstance(fahrenheit_to_celsius(test_values['test_input']), (float,int))
                self.assertAlmostEqual(fahrenheit_to_celsius(test_values['test_input']), test_values['test_output'], 1)

class TestExerciseTwo(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertTrue('celsius_to_fahrenheit' in globals())
        tests = [
            dict(test_input=10,test_output=50), 
            dict(test_input=75,test_output=167), 
            dict(test_input=245,test_output=473)
        ]
        for test_values in tests:
            with self.subTest(**test_values):
                self.assertIsInstance(celsius_to_fahrenheit(test_values['test_input']), (float, int))
                self.assertAlmostEqual(celsius_to_fahrenheit(test_values['test_input']), test_values['test_output'], 1)
