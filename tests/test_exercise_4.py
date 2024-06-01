import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise4(CustomTestCase):

    def test_dict_usage(self):
        """
        The program should not use dictionaries to solve the exercise.
        """

        self.assertNoUsesDictionary()

    def test_function_usage(self):
        """
        The program should not use functions to solve the exercise.
        """

        self.assertNotUseSelfDefinedFunctions()

    def provided_soltuion_usage(self):
        """
        The program should not use the provided solution to solve 
        the exercise.
        """

        self.assertNotUsingProvidedSolution()

    def test_case_1(self):
        """
        Prints elements with odd indices from '1,2,3,4,5,6,7,8,9' as '1,3,5,7,9'
        """
        inputs = ['1,2,3,4,5,6,7,8,9']
        output = self.run_exercise(inputs)
        expected_output = "2,4,6,8"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Prints elements with odd indices from '10,20,30,40,50' as '20,40'
        """
        inputs = ['10,20,30,40,50']
        output = self.run_exercise(inputs)
        expected_output = "20,40"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Prints elements with odd indices from '5,10,15,20,25,30' as '10,20,30'
        """
        inputs = ['5,10,15,20,25,30']
        output = self.run_exercise(inputs)
        expected_output = "10,20,30"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Prints elements with odd indices from '8,7,6,5,4,3,2,1' as '7,5,3,1'
        """
        inputs = ['8,7,6,5,4,3,2,1']
        output = self.run_exercise(inputs)
        expected_output = "7,5,3,1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Prints elements with odd indices from '1,3,5,7,9' as '3,7'
        """
        inputs = ['1,3,5,7,9']
        output = self.run_exercise(inputs)
        expected_output = "3,7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Prints elements with odd indices from '0,2,4,6,8,10' as '2,6,10'
        """
        inputs = ['0,2,4,6,8,10']
        output = self.run_exercise(inputs)
        expected_output = "2,6,10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Prints elements with odd indices from '100,200,300,400,500,600' as '200,400,600'
        """
        inputs = ['100,200,300,400,500,600']
        output = self.run_exercise(inputs)
        expected_output = "200,400,600"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Prints elements with odd indices from '1,2,3' as '2'
        """
        inputs = ['1,2,3']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Prints elements with odd indices from '7,7,7,7,7' as '7,7'
        """
        inputs = ['7,7,7,7,7']
        output = self.run_exercise(inputs)
        expected_output = "7,7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Prints elements with odd indices from '123,456,789' as '456'
        """
        inputs = ['123,456,789']
        output = self.run_exercise(inputs)
        expected_output = "456"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
