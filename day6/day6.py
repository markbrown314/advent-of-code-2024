import re

class GridRange:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.x = -1
        self.y = 0
        return self
    def __next__(self):
        self.x += 1
        if self.x >= self.max[0]:
            self.x = 0
            self.y += 1
            
        if self.y >= self.max[1]:
            raise StopIteration
        
        return (self.x, self.y)

def solution(detect_loop = False):

    with open("input.txt") as f:
        grid = f.read().strip().split("\n")

    space = set()
    past_pos = set()
    loop = set()
    home_pos = (0,0)

    max = (len(grid),len(grid[0]))
    
    for x,y in GridRange(max):
            print(x,y)
            if grid[y][x] == "#":
                space.add((x,y))
                print ("obs", (x,y))
            if grid[y][x] == "^":
                home_pos = pos = (x,y)
                angle = 0
    moves = 0
    print(space)

    print("start", pos)
    loops = 0
    if detect_loop:
        obs_locations = [*GridRange(max)]
        obs_pos = None    

    while True:
        if detect_loop and not obs_pos:
            while obs_locations:
                loop = set()
                pos = home_pos
                angle = 0
                obs_pos = obs_locations.pop()
                if obs_pos in space:
                    continue
                else:
                    #print("obs_pos", obs_pos)
                    space.add(obs_pos)
                    break
            if not obs_locations:
                return loops         
            
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
            #print(angle)
        else:
            if pos not in past_pos:
                moves += 1
            past_pos.add(pos)
            pos = next_pos
            #print(pos, moves)

            if detect_loop:
                if (pos, angle) in loop:
                    #print("you are in a loop")
                    space.remove(obs_pos)
                    obs_pos = None
                    loops += 1
                else:
                    loop.add((pos, angle))
        
            if pos[0] >= max[0] or pos[0] < 0 or pos[1] >= max[1] or pos[1] < 0:
                if not detect_loop:
                    return moves
                else:
                    space.remove(obs_pos)
                    #print("next")
                    obs_pos = None

    print(pos, moves)
if __name__ == "__main__":
    print("Part 1", solution(False))
    print("Part 2", solution(True))