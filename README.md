# TDD Python Task

##
<p align="center">
  <img src="/imgs/TDD_Diagram.PNG">
</p>
<p align="center">TDD Steps Diagram</p>

## TODO:
- create a test to check is the number divisible/remainder 0 if True pass the test if False fail
  ```python
  import unittest
  import pytest
  
  from code_tdd import Calculator
  
  class CalcTest(unittest.TestCase):

    calc = Calculator()

    def test_remainder(self):
        self.assertEqual(self.calc.remainder(15, 3), 0)
  ```
- create a class and method to write code to pass the test
  ```python
  class Calculator:

    def remainder(self, num1, num2):
        return num1 % num2
  ```
- create a test case to calculate % and code to pass the test
  #### *Test*
  ```python
  def test_percentage(self):
    self.assertEqual(self.calc.percentage(1, 5), 20.0)
  ```
  #### *Code*
  ```python
  def percentage(self, num1, num2):
    quo = num1 / num2
    return quo * 100
  ```
- create a test to check if the given values are positive
  ```python
  def test_is_positive(self):
    self.assertEqual(self.calc.is_positive(5), True)
  ```
- create a method in the class to pass the test
  ```python
  def is_positive(self, num1):
    return num1 > 0
  ```