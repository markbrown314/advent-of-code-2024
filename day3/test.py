import unittest
import day3

class TestDay3(unittest.TestCase):

    def test_part1(self):
        r = day3.solution(False, "input-test.txt")
        self.assertEqual(r, 161, "result is incorrect")
    
    def test_part2(self):
        r = day3.solution(True, "input-test2.txt")
        self.assertEqual(r, 48, "result is incorrect")

if __name__ == '__main__':
    unittest.main()