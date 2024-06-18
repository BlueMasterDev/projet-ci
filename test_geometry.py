import unittest
from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_circumference

class TestGeometry(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(10, 10), 100)
        self.assertEqual(rectangle_area(15, 5), 75)
        self.assertEqual(rectangle_area(0, 0), 0)
        
    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)
        self.assertEqual(rectangle_perimeter(2, 4), 12)
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        
    def test_circle_area(self):
        self.assertEqual(circle_area(3), 28.26)
        self.assertEqual(circle_area(6), 113.04)
        self.assertEqual(circle_area(0), 0)
        
    def test_circle_circumference(self):
        self.assertEqual(circle_circumference(5), 31.4)
        self.assertEqual(circle_circumference(8), 50.24)
        self.assertEqual(circle_circumference(0), 0)
        
if __name__ == '__main__':
    unittest.main() 