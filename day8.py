from packages.support import GridRangeFile
import itertools as it
"""
🎅🏻 Day 8: Resonant Collinearity
"""
def solution(part: int = 1, filename: str = "inputs/day8-input.txt") -> int:
    def delta(a, b):
        return (a[0] - b[0], a[1] - b[1])
    
    def add(a, b):
        return(a[0] + b[0], a[1] + b[1])

    antennas = dict()
    cdict = dict()

    for x,y,a in GridRangeFile(filename):
        if a != '.':
            antennas[a] = antennas.get(a, []) + [(x, y)]
    m = (x, y)

    for a in antennas:
        for p in it.product((c for c in antennas[a]), repeat = 2):
            if part == 2:
                cdict[p[0]] = a

            d = delta(p[0], p[1])

            while True:
                an = add(p[0], d)

                if an == p[0] or an[0] < 0 or an[1] < 0 or an[0] > m[0] or an[1] > m[1]:
                    break
                
                cdict[an] = cdict.get(an, '#')

                p = (an, None)

                if part == 1:
                    break

    return len(cdict)

if __name__ == "__main__":
    print("Part 1:", solution(1))
    print("Part 2:", solution(2))