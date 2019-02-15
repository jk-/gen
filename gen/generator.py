from gen import Instruction


class Generator(object):
    '''
        The main class that holds all the instructions.
    '''
    def __init__(self):
        self.instructions = []

    def add_instruction(self, instruction: str):
        if instruction != "":
            self.instructions.append(Instruction(instruction))

    def process(self):
        pass

    def last(self):
        return self.instructions[-1]

    def __iter__(self):
        for i in self.instructions:
            yield i

    def __len__(self):
        return len(self.instructions)
