def flatten_dict(input_dict, prefix=None):
    if prefix is None:
        prefix = []

    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            sub_dict = flatten_dict(value, prefix + [key])
            output_dict.update(sub_dict)
        else:
            output_dict['.'.join(prefix + [key])] = value

    return output_dict


def print_output(output_dict):
    result = {}
    for key, value in output_dict.items():
        parts = key.split('.')
        for i in range(len(parts)):
            if parts[i] not in result:
                result[parts[i]] = parts[i+1:]
        if value:
            result[key] = value
    return result



input_dict = {"abc": {"def": {"ghi": {"jkl": {"mno": {"pqr": {"stu": {"vwx": {"yz": "you are finally here !!!"}}}}}}}}}

output_dict = flatten_dict(input_dict)
output = print_output(output_dict)
print(output)
