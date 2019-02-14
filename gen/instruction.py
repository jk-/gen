import hashlib


class Instruction(object):
    '''
        Holds information about an instruction and its
        parent and child instructions.

        instruction str a single line of instruction
    '''
    def __init__(self, instruction: str):
        self.id = hashlib.md5(self.instruction.encode('utf-8'))
        self.instruction = instruction
        self.parent = None
        self.child = None
