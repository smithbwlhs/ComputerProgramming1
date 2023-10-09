import unittest
from geometry_fun import square_calc, circle_calc, triangle_calc


class TestGeometryFunctions(unittest.TestCase):
    def test_square_calc(self):
        # assigning the values of square_calc for 7 to perimeter and area

        perimeter, area = square_calc(7)

        # the self.assertEqual function will either return True or False
        # can change both values based on what you would like to test

        self.assertEqual(perimeter, 28)
        self.assertEqual(area, 49)

        perimeter, area = square_calc(0)
        self.assertEqual(perimeter, 0)
        self.assertEqual(area, 0)

        perimeter, area = square_calc(10)
        self.assertEqual(perimeter, 40)
        self.assertEqual(area, 100)

    def test_circle_calc(self):
        radius, circumference, area = circle_calc(7)

        # assertAlmostEqual is the same thing except it will round it for the user and if it is roundable to the number
        # it will return True or False
        # It does not have to be perfect in this case
        # the places function lets it know how many places you would like to check

        self.assertAlmostEqual(radius, 3.5, places=3)
        self.assertAlmostEqual(circumference, 21.991, places=3)
        self.assertAlmostEqual(area, 38.483, places=3)

        radius, circumference, area = circle_calc(0)
        self.assertAlmostEqual(radius, 0.0, places=3)
        self.assertAlmostEqual(circumference, 0.0, places=3)
        self.assertAlmostEqual(area, 0.0, places=3)

        radius, circumference, area = circle_calc(14)
        self.assertAlmostEqual(radius, 7.0, places=3)
        self.assertAlmostEqual(circumference, 43.981, places=3)
        self.assertAlmostEqual(area, 153.934, places=3)

    def test_triangle_calc(self):
        perimeter, area = triangle_calc(7)
        self.assertEqual(perimeter, 21)
        self.assertAlmostEqual(area, 21.218, places=3)

        perimeter, area = triangle_calc(0)
        self.assertEqual(perimeter, 0)
        self.assertEqual(area, 0)

        perimeter, area = triangle_calc(12)
        self.assertEqual(perimeter, 36)
        self.assertAlmostEqual(area, 62.354, places=3)


if __name__ == '__main__':
    unittest.main()
