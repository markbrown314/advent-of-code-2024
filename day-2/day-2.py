"""
🎅🏻 Day 2: Red-Nosed Reports
"""
def solution_day2(dampner = False):
    safe_cnt = 0
    
    with open("input.txt") as f:
        for line in f:
            attempts = []
            attempts.append(line.split())

            if dampner:
                for n in range(0, len(line.split())):
                    levels = line.split()
                    levels.pop(n)
                    attempts.append(levels)

            for levels in attempts:
                prev = None
                is_inc = False
                is_dec = False
                is_same = False
                is_safe = True
                delta = 0

                for n, level in enumerate(levels):
                    level = int(level)
                    if prev != None:
                        delta = max(delta, abs(level - prev))
                        is_inc |= level - prev > 0
                        is_dec |= level - prev < 0
                        is_same |= level == prev

                    prev = level
                    if (is_inc and is_dec) or is_same or not (delta >= 0 and delta <= 3):
                        is_safe = False
                        break

                if is_safe:
                    safe_cnt += 1
                    break
                
        return safe_cnt

if __name__ == "__main__":
    print(solution_day2(False))
    print(solution_day2(True))
