class _position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return type(other) == _position and self.x == other.x and self.y == other.y

    def __neq__(self, other):
        return not self == other

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    
class Inconsistency(Exception):
    pass

    
class _sudoku:
    def __init__(self):
        self.__squares = [ [ {1, 2, 3, 4, 5, 6, 7, 8, 9 } for x in range(0, 9) ] for y in range(0, 9) ]

    def __getitem__(self, position):
        return self.__squares[position.y][position.x]

    def __setitem__(self, position, value):
        self.__squares[position.y][position.x] = value

    def all_positions(self):
        return [ _position(x, y) for x in range(0, 9) for y in range(0, 9) ]
        
    def copy(self):
        result = _sudoku()

        for p in self.all_positions():
            result[p] = (set(self[p]) if type(self[p]) == set else self[p])

        return result

    def is_in_same_row(self, p, q):
        return p.y == q.y

    def is_in_same_column(self, p, q):
        return p.x == q.x

    def is_in_same_square(self, p, q):
        return (p.x // 3 == q.x // 3) and (p.y // 3 == q.y // 3)

    def is_in_same_group(self, p, q):
        return self.is_in_same_row(p, q) or self.is_in_same_column(p, q) or self.is_in_same_square(p, q)

    def in_same_group(self, p):
        return (q for q in self.all_positions() if p != q and self.is_in_same_group(p, q))
    
    def set(self, position, x):
        if (type(self[position]) == int and self[position] != x) or (type(self[position]) == set and x not in self[position]):
            raise Inconsistency()
        
        self[position] = x
        
        for q in self.in_same_group(position):
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

    def find_least_ambiguous(self):
        result = None
        least = 10

        for y in range(0, 9):
            for x in range(0, 9):
                p = _position(x, y)
                ns = self[p]

                if type(ns) == set and len(ns) < least:
                    result = p
                    least = len(ns)

        return result

    def is_solved(self):
        return all(type(self[p]) == int for p in self.all_positions())

    def is_inconsistent(self):
        return any(type(self[p]) == set and len(self[p]) == 0 for p in self.all_positions())

    def solve(self):
        if not self.is_solved():
            p = self.find_least_ambiguous()

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
        def char_at(p):
            if type(self[p]) == int:
                return str(self[p])
            else:
                return "."

        def row_at(y):
            return "".join( char_at( _position(x, y) ) for x in range(0, 9) )
            
        return "\n".join( row_at(y) for y in range(0, 9) )

def parse(strings):
    sudoku = _sudoku()

    for y, string in zip(range(0, 9), strings):
        for x, char in zip(range(0, 9), string):
            if char.isdigit():
                p = _position(x, y)
                sudoku.set(p, int(char))

    return sudoku

def load_from_file(filename):
    with open(filename, 'r') as file:
        return parse(file)
