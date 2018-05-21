from unittest import TestCase
from polygon import *

class TestPolygon(TestCase):
    def test_side_len(self):
        self.assertEqual(Polygon.side_len([1,1], [5,1]), 4)

    def test_perimeter(self):
        #in different cases (different figures) this method will work good if it works for 1 figure good, will be tested in Triangle
        pass

    def test_area(self):
        # in different cases (different figures) this method will work good if it works for 1 figure good, will be tested in Triangle
        pass

    def test_triangle_area(self):
        t = Triangle([1,2],[5,2],[3,4], sides_num=3)
        self.assertEqual(t.area(),4 )

    def test_triangle_perimeter(self):
        t = Triangle([1, 2], [5, 2], [3, 4], sides_num=3)
        self.assertEqual(t.perimeter(), 9.65685424949238)


    def test_Quadrilateral(self):
        q = Quadrilateral([1, 2], [5, 2], [3, 4], [2,1], sides_num=4)
        self.assertEqual(q.perimeter(), 11.404918347287666)
        self.assertEqual(q.area(), 2.0)

    def test_Pentagon(self):
        p = Pentagon([1, 2], [5, 2], [3, 4], [2, 1], [6, 5], sides_num=5)
        self.assertEqual(q.perimeter(), 21.478510929252252)
        self.assertEqual(q.area(), 6.0)

#if these work, all others will also work because all inherited from 1 class
