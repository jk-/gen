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

    def __iter__(self):
        for i in self.instructions:
            yield i
