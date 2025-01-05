"""
🎅🏻 Day 1: Historian Hysteria
"""
def main():
    list1 = []
    list2 = []
    # part 1
    with open("input.txt") as f:
        for line in f:
            a,b = line.split()
            list1.append(int(a))
            list2.append(int(b))
        print(sum([abs(x - y) for x, y in zip(sorted(list1), sorted(list2))]))
    # part 2
        s = 0
        m = {k: 0 for k in list1}
        for k in list2:
            if k in m:
                m[k] += 1
        for k in list1:
            s += m[k] * k
        print(s)

if __name__ == "__main__":
    main()