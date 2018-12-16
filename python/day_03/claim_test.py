import unittest
from claim import Claim

class TestClaim(unittest.TestCase):
    def test_get_xline(self):
        A = self.create(1, (1, 1), (3, 5))
        xline = A.xline()
        self.assertEqual(xline, (1, 4))

    def test_should_get_line_intersection_when_last_point_overlaps(self):
        A = self.create(1, (2, 2), (2, 2))
        inter = A.get_line_intersection(1, 3, A.xline())
        self.assertEqual(inter, (2, 3))

    def test_should_get_line_intersection_when_first_point_overlaps(self):
        A = self.create(1, (2, 2), (2, 2))
        inter = A.get_line_intersection(3, 5, A.xline())
        self.assertEqual(inter, (3, 4))

    def test_should_get_line_intersection_when_first_and_second_points_overlaps(self):
        A = self.create(1, (3, 3), (4, 4))
        inter = A.get_line_intersection(4, 5, A.xline())
        self.assertEqual(inter, (4, 5))

    def test_should_get_line_intersection_from_simple_test_example(self):
        A = self.create(1, (1, 3), (4, 4))
        xline = A.xline()
        self.assertEqual(xline, (1, 5))

        inter = A.get_line_intersection(3, 7, A.xline())
        self.assertEqual(inter, (3, 5))

    def test_get_overlaped_area_from_bottom_right_of_A(self):
        A = self.create(1, (1, 1), (2, 2))
        B = self.create(2, (2, 2), (2, 2))
        overlaped = A.get_overlaped_area(B)
        
        self.assertEqual(overlaped.coordinates, (2, 2))
        self.assertEqual(overlaped.dimension, (1, 1))

    def test_get_overlaped_area_from_top_left_of_A(self):
        A = self.create(2, (2, 2), (2, 2))
        B = self.create(1, (1, 1), (2, 2))
        overlaped = A.get_overlaped_area(B)
        
        self.assertEqual(overlaped.coordinates, (2, 2))
        self.assertEqual(overlaped.dimension, (1, 1))

    def test_from_simple_input(self):
        A = self.create(1, (1, 3), (4, 4))
        B = self.create(2, (3, 1), (4, 4))
        overlaped = A.get_overlaped_area(B)
        self.assertTrue(isinstance(overlaped, Claim))
        self.assertEqual(overlaped.coordinates, (3, 3))
        self.assertEqual(overlaped.dimension, (2, 2))

    def test_dont_get_overlaped_area(self):
        A = self.create(1, (1, 1), (2, 2))
        B = self.create(2, (5, 5), (10, 10))
        overlaped = A.get_overlaped_area(B)
        self.assertEqual(overlaped, None)

    def test_overlaped_inches_in_complex_case(self):
        A = self.create(1, (1, 1), (2, 2))
        B = self.create(2, (2, 2), (4, 2))
        C = self.create(3, (0, 2), (3, 1))
        D = self.create(4, (8, 2), (2, 2))
        E = self.create(5, (9, 3), (2, 2))
        ab = A.get_overlaped_area(B)
        self.assertEqual(ab.square_inches(), 1)
        ac = A.get_overlaped_area(C)
        self.assertEqual(ac.square_inches(), 2)
        bc = B.get_overlaped_area(C)
        self.assertEqual(bc.square_inches(), 1)
        de = D.get_overlaped_area(E)
        self.assertEqual(de.square_inches(), 1)

    def create(self, id, coordinates, dimension):
        return Claim(id, coordinates, dimension)

if __name__ == "__main__":
    unittest.main()
