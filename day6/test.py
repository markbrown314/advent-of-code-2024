import unittest
import day6

class TestDay5(unittest.TestCase):

    def test_part1(self):
        r = day6.solution(False, "day6/input-test.txt")
        self.assertEqual(r, 41, "result is incorrect")
    
    def test_part2(self):
        r = day6.solution(True, "day6/input-test.txt")
        self.assertEqual(r, 6, "result is incorrect")

if __name__ == '__main__':
    unittest.main()