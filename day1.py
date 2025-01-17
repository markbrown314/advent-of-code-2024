"""
🎅🏻 Day 1: Historian Hysteria
"""
def solution(part=1, filename = "inputs/day1-input.txt"):
    list1 = []
    list2 = []
    # part 1
    with open(filename) as f:
        for line in f:
            a,b = line.split()
            list1.append(int(a))
            list2.append(int(b))
        if part == 1:
            return sum([abs(x - y) for x, y in zip(sorted(list1), sorted(list2))])
    # part 2
        else:
            s = 0
            m = {k: 0 for k in list1}
            for k in list2:
                if k in m:
                    m[k] += 1
            for k in list1:
                s += m[k] * k
            return s

if __name__ == "__main__":
    print("Part 1:", solution(1))
    print("Part 2:", solution(2))
