import unittest
from main import find_cheapest_price

class TestCheapestFlightFinder(unittest.TestCase):
    def test_example_1(self):
        n = 4
        flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
        src = 0
        dst = 3
        k = 1
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 700)

    def test_no_route(self):
        n = 3
        flights = [[0,1,100],[1,2,100]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), -1)

    def test_large_k(self):
        n = 5
        flights = [[0,1,100],[1,2,100],[2,3,100],[3,4,100],[0,4,1000]]
        src = 0
        dst = 4
        k = 3
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 400)

if __name__ == '__main__':
    unittest.main()
