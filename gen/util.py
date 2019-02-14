

def open_file(file_name, code='r'):
    file = open(file_name, code)
    data = file.read()
    file.close()
    return data


def is_camel_case(value):
    return True if re.match(r'(^([A-Z]{1}[a-zA-Z]+$))', value) else False


def camel_to_snake(value):
    if is_camel_case(value):
        split = re.sub(r'([A-Z]{1})', r'_\1', value)
        split = split[1:]
        return split.lower()

    return value
