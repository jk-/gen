import re


def generate_class(name, inherit="object", body="pass", packages=""):
    file = open('core/python/class.py.tpl')
    template = file.read()
    file.close()

    packages_placeholder = r'\%packages\%'
    class_name_placeholder = r'\%name\%'
    inherit_placeholder = r'\%inherit\%'
    body_placeholder = r'\%body\%'

    template = re.sub(packages_placeholder, packages, template, flags=re.MULTILINE)
    template = re.sub(class_name_placeholder, name, template)
    template = re.sub(inherit_placeholder, inherit, template)
    template = re.sub(body_placeholder, body, template)

    return template
