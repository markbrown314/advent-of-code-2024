import itertools

def solution():

    def get_words(s, cl, dl):
        wl = []
        for c in cl:
            print("check", (c[0],c[1]), dl)
            w = ''
            for d in dl:
                x = c[0] + d[0]
                y = c[1] + d[1]
                w += s.get((x,y), '')
                print((x,y), w)
                if w:
                    wl.append(w)
        return wl

    s = dict()
    s_r = dict()

    with open("input.txt") as f:
        t_in = f.read()
    """
    t_in = "..X...\n" \
           ".SAMX.\n" \
           ".A..A.\n" \
           "XMAS.S\n" \
           ".X....\n"
    print(t_in)
    """
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
            print((x,y), c)
            s.update({(x,y):c})
            s_r[c] = s_r.get(c, []) + [(x,y)]
        x += 1
    
    wl = []
    print("X locs:", s_r['X'])
    for dl in ml:
        wl += get_words(s, s_r['X'], dl)
    print(wl.count("XMAS"))

    wl = []
    print("M locs:", s_r['M'])
    wl += get_words(s, s_r['M'], mlb)
    wl += get_words(s, s_r['S'], mlb)

    print(wl.count("MASMAS")+wl.count("SAMMAS")+wl.count("SAMSAM")+wl.count("MASSAM"))

if __name__ == "__main__":
    solution()
