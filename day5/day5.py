def solution():
    f = open("input-test.txt")
    data = f.readlines()
    page_rule = []
    page_set = set()
    page_dict = dict()
    updates = []

    for l in data:
        if "|" in l:
            page_rule.append(tuple(int(x) for x in l.split("|")))
            page_set.update([int(x) for x in l.split("|")])
        if "," in l:
            updates.append([int(x) for x in l.split(",")])


    page_dict = {x:i for i,x in enumerate(sorted(page_set))}
    #print(page_dict)
    #print(updates)

    for rule in page_rule:
        pos = [page_dict.get(rule[0]), page_dict.get(rule[1])]
        print(pos)
        if pos[0] > pos[1]:
            print("swap")
            page_dict[rule[0]] = pos[1]
            page_dict[rule[1]] = pos[0]

    middle_count = 0
    print(page_dict)
    for update in updates:
        check = [page_dict.get(x) for x in update]
        print(check, sorted(check))
        if check == sorted(check):
            middle_count += update[int(len(update)/2)]
            
    print(middle_count)
        
if __name__ == "__main__":
    solution()
