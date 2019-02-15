from gen.gen_method import generate_method
from gen.gen_class import generate_class
from gen.tokenize import tokenize
from gen.instruction import Instruction
from gen.generator import Generator
from gen.util import file_contents
from gen.util import is_camel_case
from gen.util import camel_to_snake

TOKEN_OBJECT = 'OBJECT'
TOKEN_INDENT = 'INDENT'
TOKEN_METHOD = 'METHOD'
TOKEN_VARIABLE = 'VARIABLE'
TOKEN_OBJECT_VARIABLE = 'OBJECT_VARIABLE'
TOKEN_METHOD_CREATE = 'METHOD_CREATE'
TOKEN_BUILD_IN = 'BUILD_IN'

__all__ = [
    'generate_method', 'generate_class', 'tokenize',
    'Instruction', 'Generator', 'file_contents',
    'is_camel_case', 'camel_to_snake'
]
