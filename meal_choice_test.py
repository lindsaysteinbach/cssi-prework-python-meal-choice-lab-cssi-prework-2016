import sys
import unittest

from meal_choice import *

class TestMealChoice(unittest.TestCase):

    def test_meal_choice_no_arg(self):
        self.assertEqual(meal_choice(), "Meat")

    def test_meal_choice_with_arg(self):
        self.assertEqual(meal_choice("Vegan"), "Vegan")
        self.assertEqual(meal_choice("Broccoli"), "Broccoli")


    
if __name__ == '__main__':
    unittest.main()
