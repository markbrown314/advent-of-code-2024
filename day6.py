import re
from packages.support import GridRangeFile
"""
🎅🏻 Day 6: Guard Gallivant
"""
def solution(detect_loop = False, filename = "inputs/day6-input.txt"):
    space = set()
    past_pos = set()
    loop = set()
    home_pos = (0,0)
    run_scan = True
    
    for x,y,e in GridRangeFile(filename):
            if e == "#":
                space.add((x,y))
            if e == "^":
                home_pos = pos = (x,y)
                angle = 0
    max_coord = (x,y)
    moves = 0
    loops = 0
    if detect_loop:
        obs_locations = [(-1,-1)]
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
                    space.add(obs_pos)
                    break
            if not obs_pos:
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
        else:
            if pos not in past_pos:
                moves += 1
            past_pos.add(pos)
            pos = next_pos

            if detect_loop:
                if (pos, angle) in loop:
                    loops += 1
                    space.remove(obs_pos)
                    obs_pos = None
                    continue
                else:
                    loop.add((pos, angle))
        
            if pos[0] > max_coord[0] or pos[0] < 0 or pos[1] > max_coord[1] or pos[1] < 0:
                if not detect_loop:
                    return moves
                if run_scan:
                    run_scan = False
                    obs_locations = list(past_pos)
                space.remove(obs_pos)
                obs_pos = None
                continue

if __name__ == "__main__":
    print("Part 1:", solution(False))
    print("Part 2:", solution(True))