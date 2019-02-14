import re
import os
import yaml
from dotmap import DotMap

from gen import generate_class

def is_camel_case(value):
    return True if re.match(r'(^([A-Z]{1}[a-zA-Z]+$))', value) else False

def camel_to_snake(value):

    if is_camel_case(value):
        split = re.sub(r'([A-Z]{1})', r'_\1', value)
        split = split[1:]
        return split.lower()

    return value

if __name__ == "__main__":
    file = open('app.gen')
    data = file.read()
    file.close()

    contexts = []

    # split by \n
    # contextualize the sentence by "indents"
    instructions = data.split("\n")
    for context in instructions:
        entry_point = context.split(" ")
        # can get indent context by counting ''

        # index conext

        #now remove all spaces/tabs
        flush = [x for x in entry_point if x != '']

        if len(flush):
            file_name = camel_to_snake(flush[0])
        else:
            continue

        file_name = f'codegen/{file_name}.yml'
        is_file = os.path.isfile(file_name)

        if is_file:
            file = open(file_name, 'r')
            yaml_data = file.read()
            file.close()
            configuration = yaml.load(yaml_data)
            configuration = DotMap(configuration)
        else:
            continue

        if configuration.inherits and configuration.inherits not in contexts:
            contexts.append(configuration.inherits)
            print(configuration.config)
            file_name = camel_to_snake(configuration.inherits)
            file_name = f'codegen/{file_name}.yml'
            file = open(file_name, 'r')
            yaml_data = file.read()
            file.close()

            parent_yaml = yaml.load(yaml_data)
            parent_yaml = DotMap(parent_yaml)
            template = parent_yaml.lang.python.template

            context_file = open(f'codegen/{template}', 'r')
            contents = context_file.read()
            context_file.close()

            output_file = open(f'{configuration.inherits}.py', 'w')
            output_file.write(contents)
            output_file.close()

            class_template = generate_class(
                configuration.name,
                inherit=configuration.inherits,
                packages=configuration.inherits
            )

            output_file = open(f'{configuration.name}.py', 'w')
            output_file.write(class_template)
            output_file.close()




            #
            # from TwitchConnection import TwitchConnection
            #
            # tc = TwitchConnection(
            #     configuration.config.host,
            #     configuration.config.port
            # )
            # tc.connect()
            # tc.send('PASS test\n')
            # tc.send('AUTH test\n')
            # print(tc.receive())


        # need to take a CamelCase and conert to camel_case


        # first order is a name of a template file
        #
        # TwitchBot
        #     if i dont find anything I need to assume
        #     using core library class gen
        # SocketConnection
        #     if we find something that matches a codegen template
        #     we need to parse the yml for cogen instructions
        #
        #

        # We will need to create a tokenizer for words
        # pass in an array of words that the tokenizer will
        # label
        #
        # regex to determine if something is camcelcase
        # r'(^([A-Z]{1}[a-zA-Z]+$))'  == CamcelCase
        #
        # if camcelcase look up a yml definition
        # will find the template file for the object creation
        # will parse out params and place them in init self context
        #
        # if lower case, contextualizing parent method
        #
        # if Excepts, Capture, Set use core library

        #
        # Loop through all contexts and find yml instructions
        # Loop through all yml instructions and parse dependencies
        # Loop through all yml instructions and context templates and args
        #
        #
        # need a regex to find
        #     class Name = r'class\s([a-zA-Z_]+\()'
        #     def Name = r'def\s([a-zA-Z_]+\()'
        #
        # when going deeper in context look for %s to assign args to method
