import unittest
import day1, day2, day3, day4, day5, day6, day7, day8
import sys

class TestAoC(unittest.TestCase):
    def test_day1_part1(self):
        r = day1.solution(1, "tests/day1-input-test.txt")
        self.assertEqual(r, 11, "result is incorrect")

    def test_day1_part2(self):
        r = day1.solution(2, "tests/day1-input-test.txt")
        self.assertEqual(r, 31, "result is incorrect")

    def test_day2_part1(self):
        r = day2.solution(1, "tests/day2-input-test.txt")
        self.assertEqual(r, 2, "result is incorrect")

    def test_day2_part2(self):
        r = day2.solution(2, "tests/day2-input-test.txt")
        self.assertEqual(r, 4, "result is incorrect")

    def test_day3_part1(self):
        r = day3.solution("tests/day3-input-test.txt")
        self.assertEqual(r, 161, "result is incorrect")
    
    def test_day3_part2(self):
        r = day3.solution("tests/day3-input-test2.txt")
        self.assertEqual(r, 48, "result is incorrect")

    def test_day4_part1(self):
        r = day4.solution(1, "tests/day4-input-test.txt")
        self.assertEqual(r, 18, "result is incorrect")
    
    def test_day4_part2(self):
        r = day4.solution(2, "tests/day4-input-test.txt")
        self.assertEqual(r, 9, "result is incorrect")

    def test_day5_part1(self):
        r = day5.solution(1, "tests/day5-input-test.txt")
        self.assertEqual(r, 143, "result is incorrect")
    
    def test_day5_part2(self):
        r = day5.solution(2, "tests/day5-input-test.txt")
        self.assertEqual(r, 123, "result is incorrect")

    def test_day6_part1(self):
        r = day6.solution(1, "tests/day6-input-test.txt")
        self.assertEqual(r, 41, "result is incorrect")
    
    def test_day6_part2(self):
        r = day6.solution(2, "tests/day6-input-test.txt")
        self.assertEqual(r, 6, "result is incorrect")

    def test_day7_part1(self):
        r = day7.solution(1, "tests/day7-input-test.txt")
        self.assertEqual(r, 3749, "result is incorrect")

    def test_day7_part2(self):
        r = day7.solution(2, "tests/day7-input-test.txt")
        self.assertEqual(r, 11387, "result is incorrect")

    def test_day8_part1(self):
        r = day8.solution(1, "tests/day8-input-test.txt")
        self.assertEqual(r, 14, "result is incorrect")

    def test_day8_part2(self):
        r = day8.solution(2, "tests/day8-input-test.txt")
        self.assertEqual(r, 34, "result is incorrect")

if __name__ == '__main__':
    # FIXME
    print("execute tests via: python3 -m unittest discover -v -s tests -t tests -p '*test.py'", file=sys.stderr)
