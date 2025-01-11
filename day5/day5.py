def solution(report_correct = True, file_name = "input.txt"):
    page_rule = []
    page_dict = dict()
    updates = []
    with open(file_name) as f:
        data = f.readlines()
        for l in data:
            if "|" in l:
                page_rule.append(tuple(int(x) for x in l.split("|")))
            if "," in l:
                updates.append([int(x) for x in l.split(",")])

    for before, after in page_rule:
        page_dict[before] = page_dict.get(before, []) + [after]

    middle_count = 0
    for update in updates:
        fix_count = 0
        while True:
            correct = True
            for i in range(0, len(update)-1):
                if not update[i] in page_dict or not update[i+1] in page_dict[update[i]]:
                    correct = False
                    if report_correct:
                        break
                    else:
                        update[i], update[i+1] = update[i+1], update[i]
                        fix_count += 1
                    
            if correct:
                if report_correct or (not report_correct and fix_count > 0):
                    middle_count += update[int(len(update)/2)]
                break
            if report_correct:
                break

    return middle_count
        
if __name__ == "__main__":
    print("part 1:", solution(True))
    print("part 2:", solution(False))
