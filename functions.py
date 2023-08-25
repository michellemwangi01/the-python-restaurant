def _validate_string(value):
    if isinstance(value, str):
        return value
    else:
        print(f"Value must be a string not a {type(value)}")
        return


def _validate_int(value):
    if isinstance(value, int):
        return value
    else:
        print(f"Value must be a int not a {type(value)}")
        return


def none_checker(values_array):
    for i in values_array:
        if i is None:
            return
