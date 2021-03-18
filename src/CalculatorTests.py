import unittest
from Calculator import  Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_addition_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1,2),3)
        self.assertEqual(calculator.result,3)

if __name__ == '__main__':
    unittest.main()
