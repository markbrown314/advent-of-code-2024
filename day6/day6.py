import re

def solution():

    with open("input-test.txt") as f:
        grid = f.read().strip().split("\n")

    space = set()
    past_pos = set()
    max = (len(grid),len(grid[0]))
    
    for y in range(0, max[1]):
        for x in range(0, max[0]):
            if grid[y][x] == "#":
                space.add((x,y))
                print ("obs", (x,y))
            if grid[y][x] == "^":
                pos = (x,y)
                angle = 0
    moves = 0
    print("start", pos)
    while True:
        match angle:
            case 0:
                next_pos = (pos[0], pos[1] - 1)
            case 90:
                next_pos = (pos[0] + 1, pos[1])
            case 180:
                next_pos = (pos[0], pos[1] + 1)
            case 270:
                next_pos = (pos[0]-1, pos[1])
        
        if next_pos in space:
            angle = (angle + 90) % 360
            print(angle)
        else:
            if pos not in past_pos:
                moves += 1
            past_pos.add(pos)
            pos = next_pos
            print(pos, moves)
        
        if pos[0] >= max[0] or pos[0] < 0 or pos[1] >= max[1] or pos[1] < 0:
            break

    print(pos, moves)
if __name__ == "__main__":
    solution()