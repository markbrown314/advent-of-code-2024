def solution(correctly_ordered = True):
    f = open("input.txt")
    data = f.readlines()
    page_rule = []
    page_dict = dict()
    updates = []

    for l in data:
        if "|" in l:
            page_rule.append(tuple(int(x) for x in l.split("|")))
        if "," in l:
            updates.append([int(x) for x in l.split(",")])

    for before, after in page_rule:
        page_dict[before] = page_dict.get(before, []) + [after]
    print(page_dict)

    middle_count = 0
    print(page_dict)
    for update in updates:
        print(update)
        correct = True
        if correctly_ordered:
            for i in range(0, len(update)-1):
                if not update[i] in page_dict or not update[i+1] in page_dict[update[i]]:
                    correct = False
                    break
            if correct:
                middle_count += update[int(len(update)/2)]
        else:
            update_count = 0
            while True:
                correct = True
                for i in range(0, len(update)-1):
                    if not update[i] in page_dict or not update[i+1] in page_dict[update[i]]:
                        update[i], update[i+1] = update[i+1], update[i]
                        correct = False
                        update_count += 1
                if correct:
                    if update_count > 0:
                        print("new:", update)
                        middle_count += update[int(len(update)/2)]
                    break

    print(middle_count)
        
if __name__ == "__main__":
    solution(True)
    solution(False)
