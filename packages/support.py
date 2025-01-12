def load_split_list(filename, sep=' '):
    input_list = []
    with open(filename) as f:
        for line in f:
            input_list.append(line.split(sep))
    return input_list

def load_char_list(filename):
    with open(filename) as f:
        return list(f.read())
    
def load_string(filename):
    with open(filename) as f:
        return f.read()
    
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

class GridRangeFile():
    def __init__(self, filename):
        with open(filename) as f:
            self.grid = f.read().strip().split("\n")
        self.max = (len(self.grid),len(self.grid[0]))
        self.iter = iter(GridRange(self.max))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        c = next(self.iter)
        x,y = c
        return x,y,self.grid[y][x]
