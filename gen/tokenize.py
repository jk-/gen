

class Tokenize(object):
    '''
        A class to help Tokenize instructions.
        Once we have a token of the instructions
        we can process them accordingly.


        CamelCase : OBJECT
            : INDENT
        lowercase: METHOD
        testing_method: METHOD
        `variable`: VARIABLE
        Config.test: OBJECT_VARIABLE
        ClassHere:test: METHOD_CREATE
        CAP: BUILT_IN
    '''
    def __init__(self, instruction: str):
        pass
