class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neq__(self, other):
        return not self == other

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    
class Inconsistency(Exception):
    pass

    
class Sudoku:
    def __init__(self):
        self.__squares = [ [ {1, 2, 3, 4, 5, 6, 7, 8, 9 } for x in range(0, 9) ] for y in range(0, 9) ]

    def __getitem__(self, position):
        return self.__squares[position.y][position.x]

    def __setitem__(self, position, value):
        self.__squares[position.y][position.x] = value

    def allPositions(self):
        for y in range(0, 9):
            for x in range(0, 9):
                yield Position(x, y)
        
    def copy(self):
        result = Sudoku()

        for p in self.allPositions():
            result[p] = (set(self[p]) if type(self[p]) == set else self[p])

        return result

    def isInSameRow(self, p, q):
        return p.y == q.y

    def isInSameColumn(self, p, q):
        return p.x == q.x

    def isInSameSquare(self, p, q):
        return (p.x // 3 == q.x // 3) and (p.y // 3 == q.y // 3)

    def isInSameGroup(self, p, q):
        return self.isInSameRow(p, q) or self.isInSameColumn(p, q) or self.isInSameSquare(p, q)

    def inSameGroup(self, p):
        return (q for q in self.allPositions() if p != q and self.isInSameGroup(p, q))
    
    def set(self, position, x):
        if (type(self[position]) == int and self[position] != x) or (type(self[position]) == set and x not in self[position]):
            raise Inconsistency()
        
        self[position] = x
        
        for q in self.inSameGroup(position):
            if type(self[q]) == set:
                if x in self[q]:
                    self[q].remove(x)

                    if len(self[q]) == 1:
                        self.set(q, list(self[q])[0])
                    elif len(self[q]) == 0:
                        raise Inconsistency()
            else:
                if self[q] == x:
                    raise Inconsistency()

    def findLeastAmbiguous(self):
        result = None
        least = 10

        for y in range(0, 9):
            for x in range(0, 9):
                p = Position(x, y)
                ns = self[p]

                if type(ns) == set and len(ns) < least:
                    result = p
                    least = len(ns)

        return result

    def isSolved(self):
        return all(type(self[p]) == int for p in self.allPositions())

    def isInconsistent(self):
        return any(type(self[p]) == set and len(self[p]) == 0 for p in self.allPositions())

    def solve(self):
        if not self.isSolved():
            p = self.findLeastAmbiguous()

            for n in self[p]:
                copy = self.copy()

                try:
                    copy.set(p, n)
                    result = copy.solve()

                    if result:
                        return result
                
                except Inconsistency:
                    pass

            return None
        else:
            return self

    def __str__(self):
        def charAt(p):
            if type(self[p]) == int:
                return str(self[p])
            else:
                return "."

        def rowAt(y):
            return "".join( charAt( Position(x, y) ) for x in range(0, 9) )
            
        return "\n".join( rowAt(y) for y in range(0, 9) )

def parse(strings):
    sudoku = Sudoku()

    for y, string in zip(range(0, 9), strings):
        for x, char in zip(range(0, 9), string):
            if char.isdigit():
                p = Position(x, y)
                sudoku.set(p, int(char))

    return sudoku

def loadFromFile(filename):
    with open(filename, 'r') as file:
        return parse(file)
