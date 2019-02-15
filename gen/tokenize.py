import re


def token_object(value: str):
    return re.match(r'(^([A-Z]{1}[a-zA-Z]+$))', value)


def tokenize(string: str):
    '''
        A method to help Tokenize instructions.
        Once we have a token of the instructions
        we can process them accordingly.


        CamelCase:      TOKEN_OBJECT
            :           TOKEN_INDENT
        lowercase:      TOKEN_METHOD
        testing_method: TOKEN_METHOD
        `variable`:     TOKEN_VARIABLE
        Config.test:    TOKEN_OBJECT_VARIABLE
        ClassHere:test: TOKEN_METHOD_CREATE
        CAP:            TOKEN_BUILD_IN
    '''
    pass
