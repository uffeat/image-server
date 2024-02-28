def sample_function(arg1, arg2, kwarg1=None, **kwargs):
    pass

# Function's __code__ attribute
code_object = sample_function.__code__

# Number of total positional arguments
total_positional_args = code_object.co_argcount

# Names of all positional arguments
positional_arg_names = code_object.co_varnames[:total_positional_args]

print(f"Positional argument names: {positional_arg_names}")

