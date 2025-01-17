from packages.support import GridRangeFile
import itertools as it

def solution(inline: bool, filename: str = "input.txt") -> int:
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
            if inline:
                cdict[p[0]] = a

            d = delta(p[0], p[1])

            while True:
                an = add(p[0], d)

                if an == p[0] or an[0] < 0 or an[1] < 0 or an[0] > m[0] or an[1] > m[1]:
                    break
                
                cdict[an] = cdict.get(an, '#')

                p = (an, None)

                if not inline:
                    break

    return len(cdict)

if __name__ == "__main__":
    print("Part 1", solution(False))
    print("Part 2", solution(True))