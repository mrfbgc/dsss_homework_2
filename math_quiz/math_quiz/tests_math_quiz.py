import unittest
from math_quiz import random_number_generator, random_operation_selector, question_generator


class TestMathGame(unittest.TestCase):

    def test_random_number_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation_selector(self):
        #  Test if the selected operation is coming from the following: + - *
        valid_operations = {'+', '-', '*'}
        for _ in range(100):  # Test multiple times for reliability
            result = random_operation_selector()
            self.assertIn(result, valid_operations)
        pass

    def test_question_generator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (100, 0, '*', '100 * 0', 0),
                (54, 54, '-', '54 - 54', 0),
                (0, 25, '-', '0 - 25', -25),
                (10, 0, '-', '10 - 0', 10),
                (33, 33, '*', '33 * 33', 1089),
                (89, 13, '-', '89 - 13', 76),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = question_generator(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
