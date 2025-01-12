import unittest
import day3.day3 as day3
import day5.day5 as day5
import day6.day6 as day6

class TestAoC(unittest.TestCase):
    def test_day3_part1(self):
        r = day3.solution(False, "day3/input-test.txt")
        self.assertEqual(r, 161, "result is incorrect")
    
    def test_day3_part2(self):
        r = day3.solution(True, "day3/input-test2.txt")
        self.assertEqual(r, 48, "result is incorrect")

    def test_day5_part1(self):
        r = day5.solution(True, "day5/input-test.txt")
        self.assertEqual(r, 143, "result is incorrect")
    
    def test_day5_part2(self):
        r = day5.solution(False, "day5/input-test.txt")
        self.assertEqual(r, 123, "result is incorrect")

    def test_day6_part1(self):
        r = day6.solution(False, "day6/input-test.txt")
        self.assertEqual(r, 41, "result is incorrect")
    
    def test_day6_part2(self):
        r = day6.solution(True, "day6/input-test.txt")
        self.assertEqual(r, 6, "result is incorrect")

if __name__ == '__main__':
    unittest.main()