import unittest

class TestExerciseOne(unittest.TestCase):
    def test_fibonacci(self):
        message_missing_log = """
Unable to run tests. Missing Output Log.
"""     
        messgae_not_defined = """
`{variable}` is not defined. For this challenge
please define `{variable}` as a function that 
accepts a single parameter.
"""
        messgae_not_callable = """
`{variable}` is not callable. `{variable}` was expected to be 
a function. To define a function use the reserved word `def`:

def my_function(parameter_one):
    return parameter_one
"""
        message_argument_error = """
`{variable}` should accept one positional argument. Your function
definition for `{variable}` should specify that `{variable}` accepts 
one argument. Like below:

def {variable}(num):
    ...

Here we see that after the functions name there is an argument named `num` 
inside the parenthesis. This says that the function `{variable}` must be 
called with an argument:

{variable}(2)
"""
        message_incorrect_output = """
`{variable}`'s output does not match the expected output 
when called with:

{variable}({input})
"""
        tests = [
            dict(test_input=7,test_output="0\n1\n1\n2\n3\n5\n"),
            dict(test_input=21,test_output="0\n1\n1\n2\n3\n5\n8\n13\n"),
            dict(test_input=1,test_output="0\n"),
            dict(test_input=40,test_output="0\n1\n1\n2\n3\n5\n8\n13\n21\n34\n"),
        ]
        for test in tests:
            with self.subTest(**test):
                self.assertTrue('__log__' in globals(),msg=message_missing_log)
                self.assertTrue(
                    'fibonacci' in globals(), 
                    msg=messgae_not_defined.format(
                        variable='fibonacci'
                    )
                )
                self.assertTrue(
                    callable(fibonacci), 
                    msg=messgae_not_callable.format(
                        variable='fibonacci'
                    )
                )
                try:
                    fibonacci(test['test_input'])
                except TypeError:
                    self.fail(msg=message_argument_error.format(variable='fibonacci'))

                self.assertTrue(
                    'fibonacci' in globals(), 
                    msg=messgae_not_defined.format(
                        variable='fibonacci'
                    )
                )
                self.assertTrue(
                    callable(fibonacci), 
                    msg=messgae_not_callable.format(
                        variable='fibonacci'
                    )
                )    
                global __log__
                __log__ = ''
                fibonacci(test['test_input'])
                self.assertMultiLineEqual(
                    __log__, 
                    test['test_output'],
                    msg=message_incorrect_output.format(
                        variable='fibonacci',
                        input=test['test_input']
                    )
                )