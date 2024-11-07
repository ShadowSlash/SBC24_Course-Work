
import unittest
import math

# Factorial Calculation
class Test_Factor(unittest.TestCase):
    def test_factor(self):
        self.assertEqual(factor(0), 1)
        self.assertEqual(factor(1), 1)
        self.assertEqual(factor(2), 2)
        self.assertEqual(factor(3), 6)
        self.assertEqual(factor(4), 24)
        self.assertEqual(factor(5),120)
        self.assertEqual(factor(10), 3_628_800)
        with self.assertRaises(ValueError):
            factor(-1)

def factor(num):
    if num < 0:
        raise ValueError("Must be a positive number")
    if num == 0:
        return 1
    return num * factor(num - 1)

# GCD Calculation
class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(500, 50), 50)
        self.assertEqual(gcd(25, 350), 25)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(-1, 1), 1)
        self.assertEqual(gcd(1, -5), 1)
        with self.assertRaises(ValueError):
            gcd(0, 0)

def gcd(num1, num2):
    if num1 == 0:
        raise ValueError("0 is not divisible")
    elif num2 == 0:
        raise ValueError("0 is not divisible")
    while num2 != 0:
        (num1, num2) = (num2, num1 % num2)
    return abs(num1)

# Power Calculation
class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -2), 0.25)

def power(base, exponent):
    return base ** exponent

# Sorted List Check
class TestSortList(unittest.TestCase):
    def sort_list(self):
        self.assertTrue(sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertFalse(sort_list([10, 2, 9, 1, 5, 6, 3, 8, 7, 4]))

def sort_list(list):
    return list == sorted(list)

# Nth Fibonacci Number
class TestFibonacci(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(10), 55)
        with self.assertRaises(ValueError):
            fib(-1)

def fib(num):
    if num < 0:
        raise ValueError("Input must be a positive integer")
    elif num <= 1:
        return num
    else:
        return(fib(num - 1) + fib(num - 2))

# Matrix Addition
def matrix_addition(matrix1, matrix2):
    if not (len(matrix1) == len(matrix2) and all(len(row1) == len(row2) for row1, row2 in zip(matrix1, matrix2))):
        raise ValueError("Matrices must have the same dimensions")
    return [[cell1 + cell2 for cell1, cell2 in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

class TestMatrixAddition(unittest.TestCase):
    def test_matrix_addition(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        result = [[6, 8], [10, 12]]
        self.assertEqual(matrix_addition(matrix1, matrix2), result)
        with self.assertRaises(ValueError):
            matrix_addition([[1, 2]], [[1, 2], [3, 4]])

# Area of Rectangle
class TestAreaRect(unittest.TestCase):
    def test_area_rect(self):
        self.assertEqual(area_rect(5, 10), 50)
        self.assertEqual(area_rect(3, 7), 21)
        with self.assertRaises(ValueError):
            area_rect(-1, 5)

def area_rect(length, wid):
    if length <= 0 or wid <= 0:
        raise ValueError("Numbers must be positive")
    return length * wid

# Area of Circle
class TestAreaCirc(unittest.TestCase):
    def test_area_circ(self):
        self.assertAlmostEqual(area_circ(1), math.pi)
        self.assertAlmostEqual(area_circ(2), 4 * math.pi)
        with self.assertRaises(ValueError):
            area_circ(-1)

def area_circ(rad):
    if rad <= 0:
        raise ValueError("Radius must be a positive number")
    return math.pi * (rad ** 2)

# Perfect Square Check
def is_perfect_square(num):
    if num < 0:
        raise ValueError("Input must be a non-negative integer")
    return int(math.sqrt(num)) ** 2 == num

class TestIsPerfectSquare(unittest.TestCase):
    def test_is_perfect_square(self):
        self.assertTrue(is_perfect_square(4))
        self.assertFalse(is_perfect_square(5))
        with self.assertRaises(ValueError):
            is_perfect_square(-1)

# Bonus 

# Median of List
def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n == 0:
        raise ValueError("List must not be empty")
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        mid1, mid2 = sorted_lst[n // 2 - 1], sorted_lst[n // 2]
        return (mid1 + mid2) / 2

class TestMedian(unittest.TestCase):
    def test_median(self):
        self.assertEqual(median([1, 3, 3, 6, 7, 8, 9]), 6)
        self.assertEqual(median([1, 2, 3, 4, 5, 6, 8, 9]), 4.5)
        with self.assertRaises(ValueError):
            median([])

# Area of Triangle
def area_triangle(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return 0.5 * base * height

class TestAreaTriangle(unittest.TestCase):
    def test_area_triangle(self):
        self.assertEqual(area_triangle(10, 5), 25)
        self.assertEqual(area_triangle(3, 7), 10.5)
        with self.assertRaises(ValueError):
            area_triangle(-1, 5)

if __name__ == "__main__":
    unittest.main()