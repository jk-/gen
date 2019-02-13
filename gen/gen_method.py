import re

def generate_method(name, args, body):
    file = open('core/python/method.py.tpl')
    template = file.read()
    file.close()

    name_placeholder = r'\%name\%'
    args_placeholder = r'\%args\%'
    body_placeholder = r'\%body\%'

    template = re.sub(name_placeholder, name, template)
    template = re.sub(args_placeholder, args, template)
    template = re.sub(body_placeholder, body, template)

    return template
