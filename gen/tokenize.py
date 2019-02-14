

class Tokenize(object):
    '''
        A class to help Tokenize instructions.
        Once we have a token of the instructions
        we can process them accordingly.


        CamelCase : TOKEN_OBJECT
            : TOKEN_INDENT
        lowercase: TOKEN_METHOD
        testing_method: TOKEN_METHOD
        `variable`: TOKEN_VARIABLE
        Config.test: TOKEN_OBJECT_VARIABLE
        ClassHere:test: TOKEN_METHOD_CREATE
        CAP: TOKEN_BUILD_IN
    '''
    def __init__(self, instruction: str):
        pass
