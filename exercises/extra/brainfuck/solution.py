import sys


class CompilationError(Exception):
    pass


class Brainfuck:
    def __init__(self, code, input = None, output = None):
        self.__memory = dict()
        self.__position = 0
        self.__instructions = self.__compile(code)
        self.__ip = 0
        self.__input = input or (lambda: ord(sys.stdin.read(1)))
        self.__output = output or (lambda x: print(chr(x), flush=True, end=''))

    def memory(self, n):
        if n in self.__memory:
            return self.__memory[n]
        else:
            return 0
        
    def __compile(self, code):
        result = []
        stack = []

        for index, instruction in zip(range(0,len(code)), code):
            if instruction == '+':
                result.append(self.__increment)
            elif instruction == '-':
                result.append(self.__decrement)
            elif instruction == '<':
                result.append(self.__left)
            elif instruction == '>':
                result.append(self.__right)
            elif instruction == '.':
                result.append(self.__write)
            elif instruction == ',':
                result.append(self.__read)
            elif instruction == '[':
                stack.append(len(result))
                result.append(None)
            elif instruction == ']':
                if len(stack) == 0:
                    raise CompilationError("Unmatched ]")

                def generate_jmp(i):
                    return lambda: self.__jmp(i)
                def generate_jz(i):
                    return lambda: self.__jz(i)
                
                i = stack.pop()
                result.append(generate_jmp(i))
                result[i] = generate_jz(len(result))
                

        if len(stack) != 0:
            raise CompilationError("Unmatched [")

        return result

    def __get(self):
        return self.memory(self.__position)
    
    def __put(self, x):
        self.__memory[self.__position] = x % 256
        
    def __add(self, delta):
        self.__put(self.__get() + delta)

    def __next(self):
        self.__ip += 1

    def __increment(self):
        self.__add(1)
        self.__next()
        
    def __decrement(self):
        self.__add(-1)
        self.__next()

    def __left(self):
        self.__position -= 1
        self.__next()

    def __right(self):
        self.__position += 1
        self.__next()

    def __write(self):
        self.__output(self.__get())
        self.__next()

    def __read(self):
        datum = self.__input()
        self.__put(datum)
        self.__next()

    def __jmp(self, n):
        self.__ip = n

    def __jz(self, n):
        if self.__get() == 0:
            self.__ip = n
        else:
            self.__next()

    def step(self):
        self.__instructions[self.__ip]()

    def run(self):
        while self.__ip < len(self.__instructions):
            self.step()



if __name__ == '__main__':
    code = sys.stdin.read()
    vm = Brainfuck(code)
    vm.run()
