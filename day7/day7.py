import itertools
def solution(concat=False, filename = "input-test.txt"):
    with open(filename) as f:
        lines = f.read().strip().split('\n')

    equation_list = []
    for l in lines:
        answer,nums = l.split(':')
        equation_list.append((int(answer), [int(x) for x in nums.lstrip().split(' ')]))

    total = 0
    for t, nums in equation_list:     
        ops = [*itertools.product(*['*+|' if concat else '*+'], repeat=len(nums)-1)]
        for c in ops:
            e = []
            for x,y in itertools.zip_longest(nums, c, fillvalue=':'):
                e.append(x)
                e.append(y)              
            acc = 0
            nextop = None
            for l in e:
                if l == '*':
                    nextop = '*'
                    continue
                if l == '+':
                    nextop = '+'
                    continue
                if l == '|':
                    nextop = '|'
                    continue
                if l == ':':
                    break
                if nextop == None:
                    acc = int(l)
                if nextop == '+':
                    acc += int(l)
                if nextop == '*':
                    acc *= int(l)
                if nextop == '|':
                    acc = int(str(acc)+str(l))
            if acc == t:
                total += acc
                break
    return total

if __name__ == "__main__":
    print("Part 1", solution(False, "input.txt"))
    print("Part 2", solution(True, "input.txt"))
