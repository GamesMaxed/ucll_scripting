import random
import re


class PuzzleLibrary:
    def __init__(self):
        self.__puzzles = []

    def add(self, category, puzzle):
        self.__puzzles.append( (category, puzzle) )

    def random_puzzle(self):
        category, solution = random.choice(self.__puzzles)

        return Puzzle(category, solution)


class Puzzle:
    def __init__(self, category, solution):
        def is_letter(c):
            return re.fullmatch(r'[a-zA-Z]', c)
        
        self.__category = category
        self.__puzzle = [ (char.upper(), not is_letter(char)) for char in solution ]

    @property
    def category(self):
        return self.__category
        
    def show(self):
        def show_char(c, shown):
            if shown:
                return c
            else:
                return '_'
            
        return "".join( show_char(char, shown) for char, shown in self.__puzzle )

    def is_solved(self):
        return all( shown in _, shown in self.__puzzle )

    def guess(self, letter):
        count = 0

        for i in range(0, len(self.__puzzle)):
            c, shown = self.__puzzle[i]

            if not shown and c == letter.upper():
                self.__puzzle[i] = (c, True)
                count += 1

        return count
                

