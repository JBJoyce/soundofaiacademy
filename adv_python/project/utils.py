from typing import List, Dict

from project.errors import DifferentNumberOfArgumentsError


def accepts_types(*expected_types):
    """
    Decorator that checks the arguments of a method are valid
    raises appropiate error message if otherwise
    """
    
    def check_types(func):
        def wrapper(*args, **kwargs):
            args_without_self = args[1:]
            _raise_error_if_num_of_passed_and_expected_args_dont_match(args_without_self, expected_types)
            _raise_error_if_types_of_passed_and_expected_args_dont_match(args_without_self, expected_types)
            return func(*args, **kwargs)
        return wrapper
    return check_types

def _raise_error_if_num_of_passed_and_expected_args_dont_match(passed_args, expected_types):
    if len(passed_args) != len(expected_types):
        msg = "Number of arguments passed in decorator " \
              f"{len(expected_types)} doesn't match with number of " \
              f"arguments in method, i.e., {len(passed_args)}"
        raise DifferentNumberOfArgumentsError(msg)
    
def _raise_error_if_types_of_passed_and_expected_args_dont_match(passed_args, expected_types):
    for (arg, expected_type) in zip(passed_args, expected_types):
        if not isinstance(arg, expected_type):
            raise TypeError(f"Argument '{arg}' is of type '{type(arg)}'"
                            f"Expected type '{expected_type}' instead")
                  