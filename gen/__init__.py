from gen.gen_method import generate_method
from gen.gen_class import generate_class

TOKEN_OBJECT = 'OBJECT'
TOKEN_INDENT = 'INDENT'
TOKEN_METHOD = 'METHOD'
TOKEN_VARIABLE = 'VARIABLE'
TOKEN_OBJECT_VARIABLE = 'OBJECT_VARIABLE'
TOKEN_METHOD_CREATE = 'METHOD_CREATE'
TOKEN_BUILD_IN = 'BUILD_IN'

__all__ = [
    'generate_method', 'generate_class'
]
