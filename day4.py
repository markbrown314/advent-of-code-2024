import itertools
"""
🎅🏻 Day 4: Ceres Search
"""
def solution(part = 1, filename = "inputs/day4-input.txt"):
    def get_words(s, cl, dl):
        wl = []
        for c in cl:
            w = ''
            for d in dl:
                x = c[0] + d[0]
                y = c[1] + d[1]
                w += s.get((x,y), '')
                if w:
                    wl.append(w)
        return wl

    s = dict()
    s_r = dict()

    with open(filename) as f:
        t_in = f.read()
    x = 0
    y = 0
    ml = [[(0,0),(1,0),(2,0),(3,0)],
         [(0,0),(1,1),(2,2),(3,3)],
         [(0,0),(0,1),(0,2),(0,3)],
         [(0,0),(1,-1),(2,-2),(3,-3)],
         [(0,0),(-1,0),(-2,0),(-3,0)],
         [(0,0),(-1,-1),(-2,-2),(-3,-3)],
         [(0,0),(-1,1),(-2,2),(-3,3)],
         [(0,0),(0,-1),(0,-2),(0,-3)]]

    mlb = [(0,0),(1,1),(2,2),(0,2),(1,1),(2,0)]

    for c in t_in:
        if c == '\n':
            x = 0
            y += 1
            continue
        elif c == '.':
            pass 
        else:
            s.update({(x,y):c})
            s_r[c] = s_r.get(c, []) + [(x,y)]
        x += 1
    
    
    if part == 1:
        wl = []
        for dl in ml:
            wl += get_words(s, s_r['X'], dl)

        return wl.count("XMAS")
    
    else:
        wl = []
        wl += get_words(s, s_r['M'], mlb)
        wl += get_words(s, s_r['S'], mlb)

        return wl.count("MASMAS")+wl.count("SAMMAS")+wl.count("SAMSAM")+wl.count("MASSAM")

if __name__ == "__main__":
    print("Part 1:", solution(1))
    print("Part 2:", solution(2))
