import re
import os
import yaml

from dotmap import DotMap

from gen import Generator
from gen import util


def main():
    generator = Generator()

    data = util.file_contents('app.gen')
    instructions = data.split("\n")

    for instruction in instructions:
        generator.add_instruction(instruction)

    generator.process()


if __name__ == "__main__":
    main()

    #
    # entry_point = instruction.split(" ")
    #
    # # can get indent context by counting ''
    #
    # # index conext
    #
    # #now remove all spaces/tabs
    # flush = [x for x in entry_point if x != '']
    #
    # if len(flush):
    #     file_name = camel_to_snake(flush[0])
    # else:
    #     continue
    #
    # file_name = f'codegen/{file_name}.yml'
    # is_file = os.path.isfile(file_name)
    #
    # if is_file:
    #     file = open(file_name, 'r')
    #     yaml_data = file.read()
    #     file.close()
    #     configuration = yaml.load(yaml_data)
    #     configuration = DotMap(configuration)
    # else:
    #     continue
    #
    # if configuration.inherits and configuration.inherits not in contexts:
    #     contexts.append(configuration.inherits)
    #     print(configuration.config)
    #     file_name = camel_to_snake(configuration.inherits)
    #     file_name = f'codegen/{file_name}.yml'
    #     file = open(file_name, 'r')
    #     yaml_data = file.read()
    #     file.close()
    #
    #     parent_yaml = yaml.load(yaml_data)
    #     parent_yaml = DotMap(parent_yaml)
    #     template = parent_yaml.lang.python.template
    #
    #     context_file = open(f'codegen/{template}', 'r')
    #     contents = context_file.read()
    #     context_file.close()
    #
    #     output_file = open(f'{configuration.inherits}.py', 'w')
    #     output_file.write(contents)
    #     output_file.close()
    #
    #     class_template = generate_class(
    #         configuration.name,
    #         inherit=configuration.inherits,
    #         packages=configuration.inherits
    #     )
    #
    #     output_file = open(f'{configuration.name}.py', 'w')
    #     output_file.write(class_template)
    #     output_file.close()
